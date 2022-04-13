from catalog.models import Category, Item, Tag

from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Prefetch
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
    item = get_object_or_404(Item.objects.select_related('category').prefetch_related(
        Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only('name')),
    ).only('name', 'text', 'category__name', 'tags__name'), pk=id_product, is_published=True)

    stars = Rating.objects.filter(item=item, star__in=[1, 2, 3, 4, 5]).aggregate(
        Avg('star'), Count('star'))
    try:
        star_user = Rating.objects.only('star').get(item=item, user=request.user).star
    except Rating.DoesNotExist:
        star_user = 0

    context = {
        'item': item,
        'stars': stars,
        'star_user': star_user
    }
    TEMPLATE_NAME = 'catalog/item_detail.html'
    return render(request, TEMPLATE_NAME, context)


@require_POST
@login_required
def set_star(request, id_product):
    item = get_object_or_404(Item, pk=id_product, is_published=True)
    post = request.POST.dict()
    Rating.objects.update_or_create(
        item=item,
        user=request.user,
        defaults={'star': post['star']}
    )
    return redirect('item_detail', id_product)
