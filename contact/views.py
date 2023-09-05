from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact
from .forms import ContactForm


def send_email(contact):
    """
    Send an email to the site owners with the sender's message
    """

    superusers = User.objects.filter(is_superuser=True)
    master_email = str(settings.DEFAULT_FROM_EMAIL)
    sent_by = ""

    if contact.user:
        sent_by = contact.user.username
    else:
        sent_by = "This person does not have a user profile."

    subject = f'Tubular Retro enquiry: {contact.subject}'
    body = f"Tubular Retro received an enquiry.\
            Please see details below:\n\
                User profile: {sent_by}\n\
                Email address: {contact.email}\n\
                Message: {contact.message}"

    for superuser in superusers:
        try:
            send_mail(
                subject,
                body,
                master_email,
                [str(superuser.email]
            )
            messages.success(request, "Contact form submitted.")
        except BadHeaderError:
            messages.error(
                request, "Invalid email header found. Email not sent.")
        else:
            messages.error(
                request, f"Unknown error occurred. Please contact us directly\
                    on { master_email }.")


def contact_form(request):
    """
    Send a contact form to the site admin
    """

    if request.method == 'POST':
        user=request.user
        form=ContactForm(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            if user.is_authenticated:
                contact.user=user
            form.save()
            send_email(form)
            return redirect('home')
        else:
            messages.error(
                request, 'Failed to submit form.\
                    Please check your submission.')
    else:
        form=ContactForm()

    template='contact/contact.html'

    context={
        'form': form,
    }

    return render(request, template, context)
