import random

from django.db.models import Max
from django.shortcuts import render

from catalog.models import Item


def home(request):
    context = {}

    # Не самый быстрый способ получения всех опубликованных товаров,
    #  но один из самых простых.
    ids = list(Item.objects.filter(is_published=True).values_list('id', flat=True))
    if len(ids) < 3:
        context['items'] = Item.objects.filter(is_published=True)
    else:
        context['items'] = Item.objects.filter(pk__in=random.sample(ids, 3))
    return render(request, 'homepage/home.html', context=context)
