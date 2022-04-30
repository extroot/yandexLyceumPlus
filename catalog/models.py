import random

from django.db import models
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

from sorl.thumbnail import get_thumbnail

from tinymce.models import HTMLField

from catalog.validators import text_validation
from core.models import Published, Slug
from rating.models import Rating


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

    def user_liked_items(self, user):
        return self.filter(
            pk__in=Rating.objects.filter(
                user=user, star=5).values_list('item_id')
        ).prefetch_related(
            Prefetch('tags', queryset=Tag.objects.published_tags())
        ).only('name', 'text', 'tags__name', 'category_id')

    def get_item(self, id_product):
        return get_object_or_404(
            self.select_related('category').prefetch_related(
                Prefetch('tags', queryset=Tag.objects.published_tags()),
            ).only('name', 'text', 'category__name', 'tags__name'),
            pk=id_product, is_published=True)


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
    text = HTMLField(
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

    image = models.ImageField(
        upload_to='uploads/',
        verbose_name='Изображение',
        null=True
    )

    def get_image_x1280(self):
        if self.image:
            return get_thumbnail(self.image, '1280', quality=51)
        return 'Нет изображения'

    def get_image_400x300(self):
        if self.image:
            return get_thumbnail(self.image, '400x300', crop='center',
                                 quality=51)
        return 'Нет изображения'

    def image_tmb(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50">')
        return 'Нет изображения'

    image_tmb.short_descriptions = 'Превью изображения'
    image_tmb.allow_tags = True

    objects = ItemManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Image(models.Model):
    image = models.ImageField(
        upload_to='uploads/',
        verbose_name='Изображение'
    )

    item = models.ForeignKey(
        verbose_name='Товар',
        to='Item',
        related_name='gallery',
        on_delete=models.CASCADE
    )

    def get_image_400x300(self):
        return get_thumbnail(self.image, '400x300', crop='center', quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50">')
        return 'Нет изображения'

    image_tmb.short_descriptions = 'Превью изображения'
    image_tmb.allow_tags = True

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = 'Изображение в галерее'
        verbose_name_plural = 'Изображения в галерее'


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
