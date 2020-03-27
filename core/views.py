from django.shortcuts import render
from .models import Item
# Create your views here.


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home-page.html", context)


def checkout(request):
    context = {

    }
    return render(request, "checkout-page.html", context)


def products(request):
    context = {

    }
    return render(request, "product-page.html", context)
