from django.views.generic import TemplateView

from catalog.forms import StarForm
from catalog.models import Category, Item

from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from rating.models import Rating


def item_list(request):
    categories = Category.objects.published_category()

    context = {
        'categories': categories
    }
    TEMPLATE_NAME = 'catalog/item_list.html'
    return render(request, TEMPLATE_NAME, context)


def item_detail(request, id_product):
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=id_product, is_published=True)

        form = StarForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            Rating.objects.update_or_create(
                item=item,
                user=request.user,
                defaults={'star': form.cleaned_data['star']}
            )
        return redirect('item_detail', id_product)

    item = Item.objects.get_item(id_product)

    stars = item.ratings.exclude(star=0).aggregate(
        Avg('star'), Count('star'))

    star_user = 0
    if request.user.is_authenticated:
        star_user = Rating.objects.get_user_star(item, request.user)

    context = {
        'item': item,
        'stars': stars,
        'star_user': star_user,
        'form': StarForm()
    }
    TEMPLATE_NAME = 'catalog/item_detail.html'
    return render(request, TEMPLATE_NAME, context)
