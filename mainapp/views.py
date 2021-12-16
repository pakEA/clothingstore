import os.path
import random

from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory, Product

# Create your views here.
module_dir = os.path.dirname(__file__, )


def get_menu():
    return ProductCategory.objects.all()


def index(request):
    context = {
        'page_title': 'home',
    }
    return render(request, 'mainapp/index.html', context)


def product(request, pk=None):
    products = Product.objects.all()

    context = {
        'page_title': 'shop',
        'products': products,
        'categories': get_menu(),
    }
    return render(request, 'mainapp/product.html', context)


def category(request, pk):
    get_menu()
    if pk == 0:
        _category = {'pk': 0, 'name': 'all products'}
        products = Product.objects.all()
    else:
        _category = get_object_or_404(ProductCategory, pk=pk)
        products = _category.product_set.all()

    context = {
        'page_title': 'products of the category',
        'categories': get_menu(),
        'category': _category,
        'products': products,
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


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'page_title': 'product detail',
        'product': product,
        'categories': get_menu(),
        'same_product': same_product(product),
    }
    return render(request, 'mainapp/product-detail.html', context)


def hot_product(request):
    _hot_product = random.choice(Product.objects.all())

    context = {
        'page_title': 'hot product',
        'hot_product': _hot_product,
        'same_product': same_product(_hot_product),
    }
    return render(request, 'mainapp/hot-product.html', context)


def same_product(_hot_product):
    return Product.objects.filter(category=_hot_product.category). \
                          exclude(pk=_hot_product.pk)[:4]
