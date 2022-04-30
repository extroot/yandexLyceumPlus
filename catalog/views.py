from catalog.forms import StarForm
from catalog.models import Category, Item

from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from rating.models import Rating


class ItemListView(View):
    template_name = 'catalog/item_list.html'

    def get(self, request):
        categories = Category.objects.published_category()

        context = {
            'categories': categories
        }
        return render(request, self.template_name, context)


class ItemDetailView(View):
    template_name = 'catalog/item_detail.html'

    def get(self, request, id_product):
        item = Item.objects.get_item(id_product)

        stars = item.ratings.exclude(star=0).aggregate(
            Avg('star'), Count('star')
        )

        star_user = 0
        if request.user.is_authenticated:
            star_user = Rating.objects.get_user_star(item, request.user)

        context = {
            'item': item,
            'stars': stars,
            'star_user': star_user,
            'form': StarForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, id_product):
        # Используется именно get_or_404 т.к. нам не нужны зависимости объекта.
        item = get_object_or_404(Item, pk=id_product, is_published=True)

        form = StarForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            Rating.objects.update_or_create(
                item=item,
                user=request.user,
                defaults={'star': form.cleaned_data['star']}
            )
        return redirect('item_detail', id_product)
