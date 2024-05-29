from django.shortcuts import render
from project.models import ProductForSale

def index(request):
    products = ProductForSale.objects.order_by('-id')

    context = {
        'site_title': 'Principal',
        'products': products
    }
    return render(request, 'project/index.html', context)

def product(request, id_product, name_product):
    context = {
        'site_title': 'Produto'
    }
    return render(request, 'project/product.html', context)