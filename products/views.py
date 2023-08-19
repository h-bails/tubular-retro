from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and searching """

    products = Product.objects.all()
    query = None
    category = None

    if request.GET:

        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name__iexact=category)
            category = Category.objects.filter(name__in=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter some search criteria.")
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show details of an individual product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
