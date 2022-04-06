from django.shortcuts import render

from catalog.models import Item


def item_list(request):
    all_items = Item.objects.filter(is_published=True)
    context = {
        'items': all_items
    }
    return render(request, 'catalog/item_list.html', context)


def item_detail(request, id_product):
    context = {
        "id_product": id_product
    }
    return render(request, 'catalog/item_detail.html', context)
