from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', [])

    if not bag:
        messages.error(request, "There's nothing in your bag!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NjMY1GmOOLi0vexTzVo24j0xbH1wOuyl9ngI90WWyUwSCClOL6U82Hgt4qIFXiAbONU3LNi4JA4gQKVqB3wDjqX009njjDqKy',
        'client_secret': 'test',
    }

    return render(request, template, context)
