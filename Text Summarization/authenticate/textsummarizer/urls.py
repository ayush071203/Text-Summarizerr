from django.contrib import admin
from django.urls import path , include
from app.views import home 
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    path('home/',home,name='home'),
    path('accounts/' , include('django.contrib.auth.urls')),
    path('accounts/register',views.REGISTER, name = 'register'),
    path('login/', views.dologin,name ='dologin'),
    path('',views.homepage,name = 'homepage')
]
