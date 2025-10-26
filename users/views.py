from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Product

def home(request):
    products = Product.objects.filter(is_available=True)
    context = {
        'products': products, 
    }
    return render(request, 'home.html', context)
