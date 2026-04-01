
from django.urls import include, path
from django.shortcuts import render
from .views import register_view, login_view, logout_view,profile_view,change_password
from django.contrib import admin

urlpatterns = [
   path('change-password/',change_password, name='change_password'),
    path('register/',register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
     path('profile/',profile_view, name='profile'),
   
    path('claim/',lambda request: render(request, 'claim.html'), name='claim'),
]