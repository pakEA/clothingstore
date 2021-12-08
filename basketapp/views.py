import time

from django.http import HttpResponseRedirect
from django.shortcuts import render
from basketapp.models import Basket


def index(request):
    pass


def add(request, product_pk):
    basket_item, _ = Basket.objects.get_or_create(
        user=request.user,
        product_id=product_pk
    )
    basket_item.quantity += 1
    basket_item.save()

    time.sleep(1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request, pk):
    pass
