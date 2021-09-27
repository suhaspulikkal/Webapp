from django.contrib import admin
from django.urls import path, include

from register import views
urlpatterns = [
    path('register', views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('index', views.main, name='index'),
    path('base', views.base, name='base'),
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('datas', views.datas, name='datas'),
]
