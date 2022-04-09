from catalog.models import Category, Item, Tag

from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, render


def item_list(request):
    categories = Category.objects.published_category()

    context = {
        'categories': categories
    }
    TEMPLATE_NAME = 'catalog/item_list.html'
    return render(request, TEMPLATE_NAME, context)


def item_detail(request, id_product):
    item = get_object_or_404(Item.objects.select_related('category').prefetch_related(
        Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only('name')),
    ).only('name', 'text', 'category__name', 'tags__name'), pk=id_product, is_published=True)

    context = {
        'item': item
    }
    TEMPLATE_NAME = 'catalog/item_detail.html'
    return render(request, TEMPLATE_NAME, context)
