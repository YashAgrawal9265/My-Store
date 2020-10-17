from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.index,name="home"),
    path('blogpost/<int:myid>',views.blogpost,name="blogpost")
]