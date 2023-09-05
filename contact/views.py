from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from .models import Contact
from .forms import ContactForm


def send_email(request, contact):
    """
    Send an email to the site owner with the sender's message
    """

    master_email = str(settings.DEFAULT_FROM_EMAIL)
    sent_by = ""

    if contact.user:
        sent_by = contact.user.username
    else:
        sent_by = "This person does not have a user profile."

    subject = f'Tubular Retro enquiry: {contact.subject}'
    body = f"Tubular Retro received an enquiry.\n\
            Please see details below:\n\
                User profile: {sent_by}\n\
                Email address: {contact.from_email}\n\
                Message: {contact.message}"

    try:
        send_mail(
            subject,
            body,
            master_email,
            [master_email],
        )
        messages.success(request, "Contact form submitted.")
    except BadHeaderError:
        messages.error(
            request, f"Invalid email header found. Email not sent. Please\
                contact us directly on { master_email }.")


def contact_form(request):
    """
    Send a contact form to the site admin
    """

    if request.method == 'POST':
        user = request.user
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            if user.is_authenticated:
                contact.user = user
            form.save()
            send_email(request, contact)
            return redirect('home')
        else:
            messages.error(
                request, 'Failed to submit form.\
                    Please check your submission.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
