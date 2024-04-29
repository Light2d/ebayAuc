from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404


def index(request):
    active_products = Product.objects.filter(active=True)
    completed_products = Product.objects.filter(completed=True)
    return render(request, 'index.html', {'active_products': active_products, 'completed_products': completed_products})

def product(request, product_id):
    active_products = Product.objects.filter(active=True)
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product.html', {'product': product, 'active_products': active_products})

def first_payment(request):
    return render(request, 'first_payment.html')