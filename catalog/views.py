from django.db.models import Prefetch
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from catalog.models import Item, Tag


def item_list(request):
    all_items = Item.objects.filter(is_published=True).prefetch_related(
        Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only("name"))
    )
    context = {
        'items': all_items
    }
    return render(request, 'catalog/item_list.html', context)


def item_detail(request, id_product):
    item = get_object_or_404(Item, pk=id_product)
    if not item.is_published:
        # Не уверен нужно ли это, но пусть будет.
        raise Http404()

    context = {
        'item': item
    }
    return render(request, 'catalog/item_detail.html', context)
