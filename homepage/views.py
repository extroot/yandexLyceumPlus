import random

from django.db.models import Max
from django.db.models import Prefetch
from django.shortcuts import render

from catalog.models import Item
from catalog.models import Tag


def home(request):
    context = {}

    # Не самый быстрый способ получения всех опубликованных товаров,
    #  но один из самых простых.
    # Прочитал, что .order_by('?') ненадёжен.
    ids = list(Item.objects.filter(is_published=True).values_list('id', flat=True))
    if len(ids) < 3:
        context['items'] = Item.objects.filter(is_published=True).prefetch_related(
            Prefetch('tags', queryset=Tag.objects.filter(is_published=True))
        )
    else:
        context['items'] = Item.objects.filter(pk__in=random.sample(ids, 3)).prefetch_related(
            Prefetch('tags', queryset=Tag.objects.filter(is_published=True))
        )
    return render(request, 'homepage/home.html', context=context)
