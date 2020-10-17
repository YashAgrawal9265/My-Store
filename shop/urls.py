from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('',views.index,name="home"),
    path('products/<int:myid>',views.products,name="products"),
    path('checkout',views.checkout,name="checkout"),
    path('tracker/',views.tracker,name="checkout"),
    path('search/',views.search,name="search")
]


