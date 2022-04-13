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

    stars = Rating.objects.filter(item=item).exclude(star=0).aggregate(
        Avg('star'), Count('star'))

    star_user = 0
    if request.user.is_authenticated:
        user_star_if_exist = Rating.objects.only('star').filter(item=item, user=request.user).first()
        if user_star_if_exist:
            star_user = user_star_if_exist.star

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
    if 'star' in post and post['star'] in [str(x[0]) for x in Rating.choices]:
        Rating.objects.update_or_create(
            item=item,
            user=request.user,
            defaults={'star': post['star']}
        )
    return redirect('item_detail', id_product)
