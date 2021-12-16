from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='name', max_length=64, unique=True)
    data = models.CharField(verbose_name='sign for css', max_length=25, default='*', blank=True)
    description = models.TextField(verbose_name='description', blank=True)
    is_active = models.BooleanField('active', default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'product category'
        verbose_name_plural = 'product categories'
        ordering = ['id']


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='product name', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(verbose_name='product description', blank=True)
    price = models.DecimalField(verbose_name='product price', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='quantity in stock', default=0)
    is_active = models.BooleanField('active', default=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    class Meta:
        ordering = ['category_id']


class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
