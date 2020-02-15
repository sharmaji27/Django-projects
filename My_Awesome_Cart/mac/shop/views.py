from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Contact
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
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        desc = request.POST.get('desc','')
        phone = request.POST.get('phone','')
        print(phone)
        cont = Contact(name=name,email=email,phone=phone,desc=desc)
        cont.save()
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def products(request,myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/product.html',{'product':product[0]})

def search(request):
    return HttpResponse('we are in search section')

def checkout(request):
    return render(request,'shop/checkout.html')
