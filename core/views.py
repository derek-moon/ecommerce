from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView
# Create your views here.


def products(request):
    context = {

    }
    return render(request, "products.html", context)


def checkout(request):
    context = {

    }
    return render(request, "checkout.html", context)


class HomeView(ListView):
    model = Item
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"
