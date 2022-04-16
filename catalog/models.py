import random

from catalog.validators import text_validation

from core.models import Published, Slug

from django.db import models
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404


class ItemManager(models.Manager):
    def published_items(self):
        return self.filter(is_published=True).prefetch_related(
            Prefetch('tags', queryset=Tag.objects.published_tags())
        ).only('name', 'text', 'tags__name', 'category_id')

    def get_random_items(self, random_obj_count):
        ids = list(self.filter(is_published=True).values_list('id', flat=True))
        if len(ids) < random_obj_count:
            return self.filter(is_published=True).prefetch_related(
                Prefetch('tags', queryset=Tag.objects.published_tags())
            ).only('name', 'text', 'category__name')
        return self.filter(
            pk__in=random.sample(ids, random_obj_count)).prefetch_related(
            Prefetch('tags', queryset=Tag.objects.published_tags())
        ).only('name', 'text')

    def get_item(self, id_product):
        return get_object_or_404(self.select_related('category').prefetch_related(
            Prefetch('tags', queryset=Tag.objects.published_tags()),
        ).only('name', 'text', 'category__name', 'tags__name'), pk=id_product, is_published=True)


class CategoryManager(models.Manager):
    def published_category(self):
        return self.filter(is_published=True).prefetch_related(
            Prefetch('items', queryset=Item.objects.published_items())
        ).order_by('weight').only('name')


class TagManager(models.Manager):
    def published_tags(self):
        return self.filter(is_published=True).only('name')


class Item(Published):
    name = models.CharField(max_length=150)
    text = models.TextField(
        verbose_name='Текст',
        help_text='Минимум два слова. Обязательно должно'
                  ' содержаться слово превосходно или роскошно',
        validators=[text_validation]
    )

    tags = models.ManyToManyField(
        verbose_name='Теги',
        to='Tag',
        related_name='items',
    )
    category = models.ForeignKey(
        verbose_name='Категория',
        to='Category',
        related_name='items',
        on_delete=models.RESTRICT
    )

    objects = ItemManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(Slug, Published):
    weight = models.PositiveSmallIntegerField(verbose_name='Вес', default=100)
    name = models.CharField(verbose_name='Имя', max_length=128)

    objects = CategoryManager()

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(Slug, Published):
    name = models.CharField(verbose_name='Имя', max_length=128)

    objects = TagManager()

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
