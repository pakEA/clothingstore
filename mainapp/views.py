import os.path
from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory, Product
# Create your views here.
module_dir = os.path.dirname(__file__,)


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
        category = {'pk': 0, 'name': 'all products'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = category.product_set.all()

    context = {
        'page_title': 'products of the category',
        'categories': get_menu(),
        'category': category,
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
    products = Product.objects.filter(pk=pk)

    context = {
        'page_title': 'product detail',
        'products': products,
    }
    return render(request, 'mainapp/product-detail.html', context)


def shoping_cart(request):
    context = {
        'page_title': 'shoping cart',
    }
    return render(request, 'mainapp/shoping-cart.html', context)
