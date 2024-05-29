from django.shortcuts import get_object_or_404
from django.shortcuts import render
# from django.core.paginator import Paginator
from project.models import ProductForSale

def index(request):
    products = ProductForSale.objects.order_by('-id')
    # paginator = Paginator(products, 5)

    context = {
        'site_title': 'Principal',
        'products': products
    }
    return render(request, 'project/index.html', context)

def product(request, id_product, name_product):
    obj_product = get_object_or_404(ProductForSale, pk=id_product)
    context = {
        'site_title': f'Produto {name_product}',
        'product': obj_product
    }
    return render(request, 'project/product.html', context)