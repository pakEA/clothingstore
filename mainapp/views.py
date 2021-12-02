import json
import os.path
from django.shortcuts import render
from mainapp.models import ProductCategory, Product
# Create your views here.
module_dir = os.path.dirname(__file__,)


def index(request):
    context = {
        'page_title': 'home',
    }
    return render(request, 'mainapp/index.html', context)


def product(request):
    # file_path = os.path.join(module_dir, 'fixtures/products.json')
    # products = json.load(open(file_path, encoding='utf-8'))

    products = Product.objects.all()
    product_category = ProductCategory.objects.all()
    # product_images = ProductGallery.objects.all()

    context = {
        'page_title': 'shop',
        'products': products,
        'product_category': product_category,
        # 'product_images': product_images,
    }
    return render(request, 'mainapp/product.html', context)


def contact(request):
    context = {
        'page_title': 'contact',
    }
    return render(request, 'mainapp/contact.html', context)


def about(request):
    context = {
        'page_title': 'about',
    }
    return render(request, 'mainapp/about.html', context)


def blog(request):
    context = {
        'page_title': 'blog',
    }
    return render(request, 'mainapp/blog.html', context)


def blog_detail(request):
    context = {
        'page_title': 'blog detail',
    }
    return render(request, 'mainapp/blog-detail.html', context)


def product_detail(request):
    context = {
        'page_title': 'product detail',
    }
    return render(request, 'mainapp/product-detail.html', context)


def shoping_cart(request):
    context = {
        'page_title': 'shoping cart',
    }
    return render(request, 'mainapp/shoping-cart.html', context)
