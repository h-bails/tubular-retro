from django.shortcuts import render, redirect, reverse, HttpResponse
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
        messages.success(request, "Item added to your bag.")

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Remove an item from the shopping bag """

    bag = request.session.get('bag', [])
    try:
        if item_id in bag:
            bag.remove(item_id)
            messages.success(request, "Item removed from your bag.")
        else:
            messages.error(request, "This item is not in your bag.")

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
