import random

from catalog.models import Item, Tag

from django.db.models import Prefetch
from django.shortcuts import render


def home(request):
    # Не самый быстрый способ получения всех опубликованных товаров,
    #  но один из самых простых. Прочитал, что .order_by('?') ненадёжен.
    random_obj_count = 3
    ids = list(Item.objects.filter(is_published=True).values_list('id', flat=True))
    if len(ids) < random_obj_count:
        items = Item.objects.filter(is_published=True).prefetch_related(
            Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only('name'))
        )
    else:
        items = Item.objects.filter(pk__in=random.sample(ids, random_obj_count)).prefetch_related(
            Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only('name'))
        )

    context = {
        'items': items
    }
    template = 'homepage/home.html'
    return render(request, template, context=context)
