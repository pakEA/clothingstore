"""clothingstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', mainapp.index, name='index'),
    path('product/', mainapp.product, name='product'),
    path('contact/', mainapp.contact, name='contact'),
    path('about/', mainapp.about, name='about'),
    path('blog/', mainapp.blog, name='blog'),
    path('blog_detail/', mainapp.blog_detail, name='blog_detail'),
    path('home_02/', mainapp.home_02, name='home_02'),
    path('home_03/', mainapp.home_03, name='home_03'),
    path('product_detail/', mainapp.product_detail, name='product_detail'),
    path('shoping_cart/', mainapp.shoping_cart, name='shoping_cart'),
]
