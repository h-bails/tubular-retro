from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import Consignment
from .forms import ConsignmentForm
from checkout.models import UserProfile


def send_consignment_email(consignment):
    """ Send the submitter a confirmation email """

    cust_email = consignment.user_profile.user.email

    if consignment.status == Consignment.Status.SUBMITTED:
        subject = 'We have received your consignment request'
        body = render_to_string(
            'consignments/consignment_emails/submit_email_body.txt',
            {'consignment': consignment,
             'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    elif consignment.status == Consignment.Status.APPROVED:
        subject = 'Tubular! Your consignment request has been approved'
        body = render_to_string(
            'consignments/consignment_emails/approve_email_body.txt',
            {'consignment': consignment,
             'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    elif consignment.status == Consignment.Status.DECLINED:
        subject = 'Your consignment request has been declined'
        body = render_to_string(
            'consignments/consignment_emails/decline_email_body.txt',
            {'consignment': consignment,
             'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )


@login_required
def submit_consignment(request):
    """
    Add a consignment request
    """

    if request.method == 'POST':
        form = ConsignmentForm(request.POST, request.FILES)
        if form.is_valid():
            consignment = form.save(commit=False)
            profile = UserProfile.objects.get(user=request.user)
            consignment.user_profile = profile
            consignment.save()
            messages.success(request, "Consignment request submitted.")
            send_consignment_email(consignment)
            return redirect('profile')
        else:
            messages.error(
                request, 'Failed to submit form.\
                    Please check your submission.')
    else:
        form = ConsignmentForm()

    template = 'consignments/new_consignment.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def manage_consignments(request):
    """
    Manage consignment requests (admin only)
    """
    if not request.user.is_superuser:
        return render(request, '403.html', status=403)

    consignments = Consignment.objects.all()
    template = 'consignments/manage_consignments.html'

    context = {
        'consignments': consignments,
    }

    return render(request, template, context)


@login_required
def edit_consignment(request, consignment_id):
    """
    Allows consignment creator to edit their submission
    """

    consignment = get_object_or_404(Consignment, pk=consignment_id)
    profile = UserProfile.objects.get(user=request.user)

    if consignment.status != '1':
        messages.error(request, 'Sorry, you cannot edit a consignment that has\
                        already been reviewed.')
        return redirect('profile')

    if consignment.user_profile != profile:
        return render(request, '403.html', status=403)

    if request.method == 'POST':
        form = ConsignmentForm(
            request.POST, request.FILES, instance=consignment)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Successfully edited { consignment.name }.')
            return redirect('profile')
        else:
            messages.error(
                request, 'Failed to edit consignment. Please check your\
                    submission.')
    else:
        form = ConsignmentForm(instance=consignment)

    template = 'consignments/edit_consignment.html'

    context = {
        'form': form,
        'consignment': consignment,
    }

    return render(request, template, context)


@login_required
def delete_consignment(request, consignment_id):
    """
    Allows consignment creator to delete their submission
    """
    consignment = get_object_or_404(Consignment, pk=consignment_id)
    profile = UserProfile.objects.get(user=request.user)

    if consignment.status != '1':
        messages.error(request, 'Sorry, you cannot delete a consignment that\
                        has already been reviewed.')
        return redirect('profile')

    if consignment.user_profile != profile:
        return render(request, '403.html', status=403)

    consignment.delete()
    messages.success(request, 'Request deleted!')
    return redirect('profile')


@login_required
def confirm_consignment(request, consignment_id):
    """
    Approve consignment requests (admin only)
    """
    if not request.user.is_superuser:
        return render(request, '403.html', status=403)

    consignment = get_object_or_404(Consignment, pk=consignment_id)
    user_profile = consignment.user_profile
    status = request.GET['status']

    if status == "approve":
        consignment.status = Consignment.Status.APPROVED
        consignment.save()
        messages.success(request, 'Consignment request approved.')
        send_consignment_email(consignment)
        return redirect(reverse('manage_consignments'))
    elif status == "decline":
        consignment.status = Consignment.Status.DECLINED
        messages.error(request, 'Consignment request declined.')
        consignment.save()
        send_consignment_email(consignment)
        return redirect(reverse('manage_consignments'))
    else:
        messages.error(request, "Invalid consignment status.")
        return redirect('profile')
