import json
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser


def load_from_json(file_name):
    with open(file_name, encoding='utf-8') as file:
        return json.load(file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        items = load_from_json('mainapp/json/categories.json')
        for item in items:
            ProductCategory.objects.create(**item)

        items = load_from_json('mainapp/json/products.json')
        for item in items:
            category = ProductCategory.objects.get(name=item['category'])
            item['category'] = category
            Product.objects.create(**item)

        if not ShopUser.objects.filter(username='django').exists():
            ShopUser.objects.create_superuser('django', None, 'geekbrains')
