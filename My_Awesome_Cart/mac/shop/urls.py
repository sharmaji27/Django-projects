from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index ,name='Shophome'),
    path('about/',views.about ,name='AboutUs'),
    path('contact/',views.contact ,name='ContactUs'),
    path('tracker/',views.tracker ,name='Tracker'),
    path('productView/',views.productView ,name='ProductView'),
    path('search/',views.search ,name='Search'),
    path('checkout/',views.checkout ,name='Checkout'),
    path('wishlist/',views.wishlist ,name='Wishlist'),
    ]