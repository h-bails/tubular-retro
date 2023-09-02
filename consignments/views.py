from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Consignment
from .forms import ConsignmentForm


@login_required
def submit_consignment(request):
    """
    Add a consignment request
    """

    if request.method == 'POST':
        form = ConsignmentForm(request.POST, request.FILES)
        if form.is_valid():
            consignment = form.save()
            messages.success(request, "Consignment request submitted.")
            return redirect('profile')
        else:
            messages.error(request, 'Failed to submit form. Please check your submission.')
    else:
        form = ConsignmentForm()  

    template = 'consignments/new_consignment.html'

    context = {
        'form': form,
    }

    return render(request, template, context)