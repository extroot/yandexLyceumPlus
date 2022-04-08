from catalog.models import Item, Tag

from django.db.models import Prefetch
from django.http import Http404
from django.shortcuts import get_object_or_404, render


def item_list(request):
    all_items = Item.objects.filter(is_published=True).prefetch_related(
        Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only('name'))
    )

    context = {
        'items': all_items
    }
    template = 'catalog/item_list.html'
    return render(request, template, context)


def item_detail(request, id_product):
    item = get_object_or_404(Item, pk=id_product)
    if not item.is_published:
        # Не уверен нужно ли это, но пусть будет.
        raise Http404()

    context = {
        'item': item
    }
    template = 'catalog/item_detail.html'
    return render(request, template, context)
