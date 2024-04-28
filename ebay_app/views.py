from django.shortcuts import render
from .models import Product


def index(request):
    active_products = Product.objects.filter(active=True)
    completed_products = Product.objects.filter(completed=True)
    return render(request, 'index.html', {'active_products': active_products, 'completed_products': completed_products})
