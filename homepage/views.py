from catalog.models import Item

from django.shortcuts import render


def home(request):
    RANDOM_OBJ_COUNT = 3

    items = Item.objects.get_random_items(random_obj_count=RANDOM_OBJ_COUNT)

    context = {
        'items': items
    }
    TEMPLATE_NAME = 'homepage/home.html'
    return render(request, TEMPLATE_NAME, context=context)
