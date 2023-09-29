from django.shortcuts import render, get_object_or_404
from products.models import Category


def index(request):
    """ A view to return the index page """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'home/index.html', context)


def about(request):
    """ A view to return the about us page """

    return render(request, 'home/about.html')
