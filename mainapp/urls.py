from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('product/', mainapp.product, name='product'),
    path('contact/', mainapp.contact, name='contact'),
    path('about/', mainapp.about, name='about'),
    path('blog/', mainapp.blog, name='blog'),
    path('blog_detail/', mainapp.blog_detail, name='blog_detail'),
    path('product_detail/', mainapp.product_detail, name='product_detail'),
    path('product_detail/<int:pk>/', mainapp.product_detail, name='product_detail'),
    path('shoping_cart/', mainapp.shoping_cart, name='shoping_cart'),
    path('category/<int:pk>/', mainapp.category, name='category'),
]
