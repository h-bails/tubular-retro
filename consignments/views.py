from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Consignment
from .forms import ConsignmentForm
from checkout.models import UserProfile


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
            return redirect('profile')
        else:
            messages.error(
                request, 'Failed to submit form. Please check your submission.')
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
                request, 'Failed to edit consignment. Please check your submission.')
    else:
        form = ConsignmentForm(instance=consignment)

    template = 'consignments/edit_consignment.html'

    context = {
        'form': form,
        'consignment': consignment,
    }

    return render(request, template, context)
