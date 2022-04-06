from django.http import Http404
from django.shortcuts import render

from catalog.models import Item


def item_list(request):
    all_items = Item.objects.filter(is_published=True)
    context = {
        'items': all_items
    }
    return render(request, 'catalog/item_list.html', context)


def item_detail(request, id_product):
    try:
        item = Item.objects.get(pk=id_product)
        if not item.is_published:
            raise Http404()
    except Item.DoesNotExist:
        raise Http404()

    context = {
        "item": item
    }
    return render(request, 'catalog/item_detail.html', context)
