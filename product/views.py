from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all() #queryset https://docs.djangoproject.com/en/5.0/ref/models/querysets/
    products_ordered_by_price = Product.objects.all().order_by("price") #order_by  https://docs.djangoproject.com/en/5.0/ref/models/querysets/#order-by
    filter_product = Product.objects.filter(name = "database") #filter https://docs.djangoproject.com/en/5.0/ref/models/querysets/
    context = {
        'products' : products,
        'filter_product' : filter_product,
        'products_ordered_by_price' : products_ordered_by_price,
    }
    return render(request,'index.html',context)

    