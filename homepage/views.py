from catalog.models import Item

from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = 'homepage/home.html'
    RANDOM_OBJ_COUNT = 3

    def get(self, request):
        items = Item.objects.get_random_items(random_obj_count=self.RANDOM_OBJ_COUNT)
        context = {
            'items': items
        }
        return render(request, self.template_name, context=context)
