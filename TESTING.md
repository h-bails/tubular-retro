
# How **Tubular Retro** was tested

Back to [README.md](README.md)<br>


## Manual Testing

I manually inspected each feature or component of the application to ensure they were functioning as anticipated. Each user story had specific user acceptance criteria that needed to be met for the feature to be successfully implemented. 

<details>
  <summary>Epic: Products and product management</summary>
  
  ### User Story: View Product Listings
  * As a user/shopper, I want to view a list of products with their images and descriptions, so I can explore what the shop offers.
  * **Acceptance Criteria**:
    * Products are displayed with a title, image, and brief description.
    * Products are displayed in a grid format that is mobile responsive.
    * The user can easily scroll through the list and quickly navigate back to the top.
  * Result: **PASS**
  
  ### User Story: View Product Details
  * As a user/shopper, I want to view the details of a product, including images, description, price, and availability.
  * **Acceptance Criteria**:
    * Clicking on a product opens a detailed view.
    * Product details include an image, a description, price, condition and measurements.
    * An option to add the product to the bag is available.
  * Result: **PASS**
  
  ### User Story: Filter Products
  * As a user/shopper, I want to filter products by category so I can narrow down my search results, or search for results using a keyword.
  * **Acceptance Criteria**:
    * Filter options and a search bar are clearly presented in the top nav.
    * Products can be filtered by category, and by keyword.
    * The filtered results are correctly displayed after selections are made.
    * The user can easily clear filters.
  * Result: **PASS**
  
  ### User Story: Sort Products
  * As a user/shopper, I want to sort products by prices, so I can find items in my budget.
  * **Acceptance Criteria**:
    * Sort options are clearly presented on the product listing page.
    * Products can be sorted in ascending or descending order by price, name, or category.
    * Correctly sorted results appear after the user action.
  * Result: **PASS**

</details>
<br>
<details>
  <summary>Epic: E-commerce Functionality</summary>
  
  ### User Story: Add Products to Bag
  * As a user/shopper, I want to add products to my bag and proceed to checkout, so I can make a purchase using Stripe for payment processing.
  * **Acceptance Criteria**:
    * Products can be added to the bag from the product details page.
    * User receives confirmation when item is added to the bag.
    * The bag updates in real-time to reflect the items added.
    * User can easily navigate to the bag page from anywhere on the site.
  * Result: **PASS**
  
  ### User Story: Remove Products from Bag
  * As a user/shopper, I want to remove products from my basket if I change my mind.
  * **Acceptance Criteria**:
    * Each product in the bag has a visible option to remove it.
    * Total price and item list adjust accordingly when items are removed.
    * User receives a note if their bag is empty.
  * Result: **PASS**
  
  ### User Story: Proceed to Checkout
  * As a user/shopper, I want to proceed to the checkout process from my basket, so I can complete my purchase.
  * **Acceptance Criteria**:
    * A clear option to proceed to checkout is available on the bag page.
    * User is able to check out whether or not they are logged in.
    * Shipping, billing, and payment details are collected via a form on the checkout page.
  * Result: **PASS**
  
  ### User Story: Review Order Summary
  * As a user/shopper, I want to see my order summary before finalizing the purchase, so I can review my selection and total cost.
  * **Acceptance Criteria**:
    * Order summary includes a list of products, their individual prices, total cost, and applicable shipping fees.
  * Result: **PASS**
  
  ### User Story: Make Payment with Stripe
  * As a user/shopper, I want to make a payment using Stripe for a seamless and secure checkout process.
  * **Acceptance Criteria**:
    * Payment details are securely collected through Stripe's API.
    * User receives feedback on successful or unsuccessful payment.
    * Order is not finalized until payment is confirmed.
    * Stripe successfully processes payment via webhooks.
  * Result: **PASS**
  
  ### User Story: Receive Order Confirmation
  * As a user/shopper, I want to receive an order confirmation with details of my purchase after completing the payment.
  * **Acceptance Criteria**:
    * User is directed to an order confirmation page after payment.
    * Confirmation page includes order details, and a unique order number.
    * An order confirmation email is sent to the user's registered email address.
  * Result: **PASS**

</details>
<br>
<details>
  <summary>Epic: User Authentication</summary>
  
  ### User Story: Register for an Account
  * As a user, I want to register for an account, so I can access my details and manage my consignment submissions.
  * **Acceptance Criteria**:
    * Users are provided a clear registration form.
    * The form collects necessary details such as username, email, and password.
    * Users receive feedback on successful registration or errors (e.g. email already registered, mismatched passwords)
    * Users are prompted to verify their email address.
    * Upon successful registration and verification, users are able to log in.
  * Result: **PASS**
  
  ### User Story: Log In to Account
  * As a user, I want to log in to my account, so I can access my profile and past orders.
  * **Acceptance Criteria**:
    * Users are provided a clear login form with fields for email and password.
    * Forgotten password option is clearly available.
    * Users receive feedback on successful login or errors (e.g., incorrect password).
  * Result: **PASS**
  
  ### User Story: Reset Password
  * As a user, I want to reset my password if I forget it, so I can regain access to my account.
  * **Acceptance Criteria**:
    * Users can easily find and access the "Forgot Password" option.
    * Users receive an email with a secure link or code to reset their password.
    * Users are able to successfully reset their password and log in with the new one.
  * Result: **PASS**
  
  ### User Story: Log out of account
  * As a user, I want to log out of my account when I finish browsing.
  * **Acceptance Criteria**:
    * Log out option is clearly visible and accessible from the user profile or menu.
    * Upon selecting "Log Out," the session ends and user is redirected to a public page.
    * User data or session details are not accessible after logging out.
  * Result: **PASS**

</details>
<br>
<details>
  <summary>Epic: Consignment Management</summary>
  
  ### User Story: Submit Item for Consignment
  * As a user, I want to submit an item for consignment by filling out a form with product details, so I can sell my items through the shop.
  * **Acceptance Criteria**:
    * Users are provided with a clear form to submit item details, including name, description, image.
    * Confirmation or feedback is provided upon successful submission.
    * The submitted item can be edited or deleted, until approved by an admin.
  * Result: **PASS**
  
  ### User Story: View Consignment Submissions Status
  * As a user, I want to know the status of my consignment submissions, so I know whether they have been approved or not.
  * **Acceptance Criteria**:
    * Users can easily navigate to a section or page listing their consignment submissions.
    * Each submission displays its current status (e.g., "Pending Review," "Approved," "Declined").
    * The user receives confirmation emails upon consigmnent submission, approval, and decline.
  * Result: **PASS**
  
  ### User Story: Edit Consignment Submissions
  * As a user, I want to edit my consignment submissions (before approval), so I can make changes to the product details if needed.
  * **Acceptance Criteria**:
    * Users can easily find an edit option for each of their pending consignment submissions.
    * Edits are saved and reflected upon submission.
  * Result: **PASS**
  
  ### User Story: Delete Consignment Submissions
  * As a user, I want to delete my consignment submissions (before approval), so I can remove items I no longer want to consign.
  * **Acceptance Criteria**:
    * Users can easily find a delete option for each of their pending consignment submissions.
    * A confirmation prompt appears before deletion.
    * Once deleted, the submission is removed from the list and the database.
  * Result: **PASS**

</details>
<br>
<details>
  <summary>Epic: Admin Functionality</summary>
  
  ### User Story: Review and Approve Consignment Submissions
  * As an admin, I want to review and approve consignment submissions, so only appropriate items are displayed on the website for sale.
  * **Acceptance Criteria**:
    * Admins can access a page listing all consignment submissions.
    * Each submission provides information and an option to approve or reject.
  * Result: **PASS**
  
  ### User Story: Reject Consignment Submissions
  * As an admin, I want to reject consignment submissions if they are not appropriate for the shop.
  * **Acceptance Criteria**:
    * Admins can reject consignment requests from the requests page.
    * The user is notified of the rejection and provided with the given reason.
  * Result: **PASS**
  
  ### User Story: Manage Products
  * As an admin, I want to be able to create, edit, and delete product listings from the admin panel.
  * **Acceptance Criteria**:
    * Admins have clear options in the nav to create new product listings.
    * Existing product listings can be edited or deleted.
    * All changes reflect immediately on the product listing page.
  * Result: **PASS**
</details>
<br>
<details>
  <summary>Epic: User Profile</summary>
  
  ### User Story: View User Information
  * As a user, I want to view and update my default delivery information from my profile page.
  * **Acceptance Criteria**:
    * The profile page clearly displays the default shipping address.
    * Users have an option to edit and save changes to their details.
    * Upon updating, the user receives feedback indicating successful changes.
  * Result: **PASS**
  
  ### User Story: View Order History
  * As a user, I want to view my order history, so I can see the details of my past purchases.
  * **Acceptance Criteria**:
    * The profile page has a section or tab dedicated to order history.
    * Past orders are listed with relevant details such as product names, date of purchase, total amount.
    * Users can click on an order to view more detailed information if needed.
  * Result: **PASS**

</details>

## Stripe payments

All payments were successfully handled by Stripe webhooks at the time of release.
## Accessibility

I ran the program through the AIM accessibility checker to ensure the site adhered to WCAG best practices.

See the results [here](https://wave.webaim.org/report#/https://tubularretro-71f0ca94931e.herokuapp.com/).
## Responsiveness

I ensured that the application was responsive by checking its look and functionality across a variety of devices and screen sizes. The site was designed in a mobile-first manner using standard Bootstrap breakpoints.

## Compatability

This application has been tested on the following web browsers:

- Chrome
- Firefox
- Safari

and operating systems:

- Windows
- macOS


## Performance

I ran a Lighthouse report to make sure that the application responded quickly. See the results for the [Homepage](https://pagespeed.web.dev/analysis/https-tubularretro-71f0ca94931e-herokuapp-com/fmb7xj6lh7?form_factor=desktop) and [All Products](https://pagespeed.web.dev/analysis/https-tubularretro-71f0ca94931e-herokuapp-com-products/9mwcvs6iby?form_factor=desktop) pages.
## Bugs fixed

I fixed several bugs during the course of the project.

- At a stage in development my dev container got corrupted. Dev container files somehow ended up inside my Checkout folder (likely admittedly to a user error on my part). I ended up having to roll back to a previous commit and rebuilding the workspace and database.
- I was also struggling with duplicate orders reflecting on the database at one stage. This was caused by a typo in my Stripe client_id value on the front end of the app. Views.py gets the Stripe client secret from the client side (template), and it wasn't able to pull that value due to the incorrect syntax. This lead to no Stripe pid linked to the orders created in views.py, so when the webhook handler searched for an existing order, the pids didn't match up and it created a new order. 


## Known bugs not yet fixed

### Timing of orders and potential for an item to be sold twice
Items sold on Tubular are one-offs, and are thus removed from the products display and the 'Add to Cart' button is disabled once they're sold. However, a technical gap still exists in this version of the code: if one user adds an item to their cart and another purchases it before checkout is completed, the item might be 'double-sold'. 

Due to challenges faced with the above duplicate order issue (which was fixed but cost significant development time), I couldn't hard-code an 'is_sold' check into the checkout and webhook handler logic before the project hand-in. 

Notably, most PP5 sample projects do seem to work on an 'unlimited' inventory model, and real-world inventory management is not a pass requirement for the project. Hence, I opted to leave this quite specific bug unfixed in the MVP, planning to enhance it in future updates.