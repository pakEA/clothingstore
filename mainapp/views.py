from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'page_title': 'home',
    }
    return render(request, 'mainapp/index.html', context)


def product(request):
    context = {
        'page_title': 'shop',
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


def home_02(request):
    context = {
        'page_title': 'home 02',
    }
    return render(request, 'mainapp/home-02.html', context)


def home_03(request):
    context = {
        'page_title': 'home 03',
    }
    return render(request, 'mainapp/home-03.html', context)


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
