import random

from catalog.models import Item, Tag

from django.db.models import Prefetch
from django.shortcuts import render


def home(request):
    # Не самый быстрый способ получения всех опубликованных товаров,
    #  но один из самых простых. Прочитал, что .order_by('?') ненадёжен.
    RANDOM_OBJ_COUNT = 3
    ids = list(Item.objects.filter(is_published=True).values_list('id', flat=True))
    if len(ids) < RANDOM_OBJ_COUNT:
        items = Item.objects.filter(is_published=True).prefetch_related(
            Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only('name'))
        ).only('name', 'text', 'category__name')
    else:
        items = Item.objects.filter(pk__in=random.sample(ids, RANDOM_OBJ_COUNT)).prefetch_related(
            Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only('name'))
        ).only('name', 'text')

    context = {
        'items': items
    }
    TEMPLATE_NAME = 'homepage/home.html'
    return render(request, TEMPLATE_NAME, context=context)
