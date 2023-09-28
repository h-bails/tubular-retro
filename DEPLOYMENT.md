# Project Setup and Deployment

This guide will walk you through the process of setting up and deploying the Tubular project locally in an Integrated Development Environment (IDE) and on Heroku.

I personally made the decision to deploy the project to Heroku early to avoid any issues with databases and environment variables later down the line, and would recommend this approach to other developers.

## Cloning the Project

- **Fork the Repository:** Start by forking the Tubular repository to your GitHub account. This provides you with your own copy of the project to work on.
- **Clone the Repository:** Once forked, clone your repository to your local machine. Use the following command to clone it:

    ```bash
    git clone https://github.com/your-username/tubular-curated-vintage.git
    ```

## Setting Up Locally

### 1. Requirements

Make sure you have the following installed:

- **Python:** 3.8 or higher. You can download it from python.org
- **Pip:** used to install and update packages. You’ll need to make sure you have the latest version of pip installed. Use the below commnand:

```bash
python3 -m pip install --user --upgrade pip
```

### 2. Create a Virtual Environment

Navigate to your desired project directory and create a venv.

```bash
python3 -m venv env
```

The second argument is the location to create the virtual environment. Generally, you can just create this in your project and call it env.

venv will create a virtual Python installation in the env folder.

Note: You should exclude your virtual environment directory from your version control system using .gitignore.

[Here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) are more detailed instructiosn on making and usinv virtual environments.

### 3. Set Environment Variables

In the project's settings (`env/settings.py`), you'll find various environment variables that need to be set. Here are some key variables:

- **SECRET_KEY:** Generate a secret key for your Django project. You can use online generators like Djecrety to do this.
- **DEBUG:** Set it to True for local development and debugging, and False for production.
- **Stripe keys:** You'll need to set `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY`. Create a Stripe account to get your keys. [Here](https://stripe.com/docs/keys#:~:text=You%20can%20find%20your%20secret,you%20can%20see%20these%20values) are instructions to create a Stripe account and getting your keys. You'll also need to [create a webhook endpoint](https://stripe.com/docs/development/dashboard/register-webhook) for your site.
- **AWS keys:** If you plan to use AWS S3 for static and media files storage, set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_STORAGE_BUCKET_NAME`. Code Institute provides a great guide on how to do this [here](https://codeinstitute.s3.amazonaws.com/fullstack/AWS%20changes%20sheet.pdf).
- **Email settings:** In a development/DEBUG environment, the project is set up to simply print emails to the terminal. No further action is needed.

The project uses `import os` and the `os.environ.get` function to get the Stripe and AWS environment variables (as well as email, in production only) from an `env.py` file or Heroku's Config Vars.

In a local environment, you'll need to create an `env.py` file in the project's root directory and add your environment variables:

```bash
SECRET_KEY=your_secret_key
DEBUG=True
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WH_SECRET=your_stripe_webhook_key
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
```

### 4. A note on databases

I reconnend Sqlite to be used in a development environment and ElephantSQL in production, but you can use the provider of your choice.

If you’re using SQLite, you don’t need to create anything beforehand - the database file will be created automatically when it is needed.

[Here](https://docs.djangoproject.com/en/4.2/ref/databases/) is the official Django documentation on how to set up other databases of your choice.

### 5. Apply Migrations

Run the following commands to apply database migrations:

```bash
    python manage.py makemigrations
    python manage.py migrate
```

### 6. Create Superuser (Optional)

To access the Django admin panel, create a superuser account:

```bash
    python manage.py createsuperuser
```
## Setting Up in Heroku

### 1. Heroku requirements

If you don't have a Heroku account, [sign up at Heroku](https://www.heroku.com/).

When you deploy to Heroku, the dependencies you specify in your `requirements.txt` file are automatically installed before app startup. Use `pip freeze > requirements.txt` in your dev environment to make sure the package versions you've installed are correctly reflected in `requirements.txt`.


### 2. Heroku CLI

The quickest way to set up this project in Heroku is to [install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) in your environment, but you can also follow the following steps directly from your Heroku dashboard.

### 3. Log in to Heroku

Open your terminal and log in to Heroku using the following command:

```bash
heroku login
```

### 4. Create a Heroku App

Create a new Heroku app with a unique name:
```bash
heroku create your-app-name
```

### 5. Configure Environment Variables

There are various environment variables that need to be set for Heroku. 

- **SECRET_KEY:** Generate a secret key for your Django project. You can use online generators like Djecrety to do this.
- **DEBUG:** Set it to False for production.
- **Stripe keys:** You'll need to set `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY`. If you did not do so previously, create a Stripe account to get your keys. [Here](https://stripe.com/docs/keys#:~:text=You%20can%20find%20your%20secret,you%20can%20see%20these%20values) are instructions to create a Stripe account and getting your keys. You'll also need to [create a webhook endpoint](https://stripe.com/docs/development/dashboard/register-webhook) for your site and take note of the webhook key.
- **AWS keys:** If you have not done so already, set up your `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_STORAGE_BUCKET_NAME`. Code Institute provides a great guide on how to do this [here](https://codeinstitute.s3.amazonaws.com/fullstack/AWS%20changes%20sheet.pdf). Note that the AWS bucket name, region, custom domain and object parameters will need to be set up directly in `settings.py`. 
- **Email settings:**  Configure email settings such as `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, and `EMAIL_HOST_PASSWORD` to enable email functionality in the live project. I used Gmail for this, but you can use the email provider of your choice. [Here](https://www.abstractapi.com/guides/django-send-email) is a handy guide covering Gmail setup, and [here](https://docs.djangoproject.com/fr/2.2/topics/email/) is the official Django send_email documentation which can be applied to any email provider.
- **Database URL:**: To generate a managed PostgreSQL database, visit the ElephantSQL website and either create a new account or log in to your existing account. After logging in, [create a new instance](https://www.elephantsql.com/docs/index.html) and take note of the URL.

You can easily set the environment variables on Heroku using the `heroku config:set` command for each variable:

```bash
heroku config:set SECRET_KEY=your_secret_key
heroku config:set DEBUG=False
heroku config:set STRIPE_PUBLIC_KEY=your_stripe_public_key
heroku config:set STRIPE_SECRET_KEY=your_stripe_secret_key
heroku config:set STRIPE_WH_SECRET=your_stripe_webhook_key
heroku config:set AWS_ACCESS_KEY_ID=your_aws_access_key
heroku config:set AWS_SECRET_ACCESS_KEY=your_aws_secret_key
heroku config:set AWS_STORAGE_BUCKET_NAME=your_bucket_name
heroku config:set EMAIL_HOST=your_email_host
heroku config:set EMAIL_PORT=your_email_port
heroku config:set EMAIL_HOST_USER=your_email_username
heroku config:set EMAIL_HOST_PASSWORD=your_email_password
heroky config:set DATABASE_URL=your_database_url
```

Or you can do this via the Heroku dashboard.

### 6. Push to Heroku

Push your code to the Heroku app's repository:
```bash
git push heroku main
```

### 7. Run Migrations and Create Superuser (Optional)

Run the database migrations and create a superuser (if needed) on Heroku:

```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

You should have successfully deployed Tubular to Heroku. [Here](https://devcenter.heroku.com/articles/deploying-python) is the official Heroku documentation if support is needed.

