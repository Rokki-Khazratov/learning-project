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
        #git test
    }
    return render(request,'index.html',context)

def product_detail(request,product_id):
    product = Product.objects.filter(id = product_id)
    context = {
        'product':product
    }
    return render(request,'product_detial.html',context)