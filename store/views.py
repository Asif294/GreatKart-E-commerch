from django.shortcuts import render
from store.models import Product

def store(request):
    products = Product.objects.filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'store.html', context)
