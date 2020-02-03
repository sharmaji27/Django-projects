from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil

def index(request):
    allprods=[]
    categories = Product.objects.values('category','id')
    cats = {item['category'] for item in categories}
    for cat in cats:
        prods = Product.objects.filter(category=cat)
        n = len(prods)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prods,range(1,nSlides),nSlides])

    params = {'allprods':allprods}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse('we are in contact section')

def tracker(request):
    return HttpResponse('we are in tracker section')

def productView(request):
    products = Product.objects.all()
    return render(request,'shop/product.html',{'products':products})

def search(request):
    return HttpResponse('we are in search section')

def checkout(request):
    return HttpResponse('we are in checkout section')

def wishlist(request):
    return HttpResponse('we are in wishlist section')

