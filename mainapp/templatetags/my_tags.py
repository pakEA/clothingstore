from django import template

from clothingstore import settings

register = template.Library()


@register.filter(name='media_folder_products')
def media_folder_products(string):
    if not string:
        string = 'products_images/default.jpg'

    return f'{settings.MEDIA_URL}{string}'


@register.filter(name='media_folder_users')
def media_folder_users(string):
    if not string:
        string = 'avatars/default.jpg'

    return f'{settings.MEDIA_URL}{string}'
