from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add an item to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', [])

    if item_id in bag:
        messages.error(request, f"{product.name} is already in your bag.")
    elif product.is_sold is True:
        messages.error(request, f"{product.name} is not available.")
    else:
        bag.append(item_id)
        messages.success(request, f"You added {product.name} to your bag.")

    request.session['bag'] = bag

    if redirect_url is None:
        return redirect(redirect_url)
    else:
        return redirect('home')


def remove_from_bag(request, item_id):
    """ Remove an item from the shopping bag """

    bag = request.session.get('bag', [])

    try:
        product = get_object_or_404(Product, pk=item_id)
        if item_id in bag:
            bag.remove(item_id)
            messages.warning(
                request, f"{product.name} was removed from your bag.")
        else:
            messages.error(request, f"{product.name} is not in your bag.")

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
