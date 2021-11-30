from django.contrib import admin
from mainapp.models import ProductCategory, Product
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)


# class GalleryInline(admin.TabularInline):
#     fk_name = 'product'
#     model = ProductGallery
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [GalleryInline, ]
