# Generated by Django 3.2.9 on 2021-11-25 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category_id']},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['id'], 'verbose_name': 'product category', 'verbose_name_plural': 'product categories'},
        ),
    ]
