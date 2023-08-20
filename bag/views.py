from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add an item to the shopping bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', [])

    if item_id in bag:
        messages.error(request, "This item is already in your bag.")
    else:
        bag.append(item_id)

    request.session['bag'] = bag
    return redirect(redirect_url)
