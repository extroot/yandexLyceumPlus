from django.db import models

from catalog.validators import text_validation
from core.models import Published, Slug


class Item(Published):
    name = models.CharField(max_length=150)
    text = models.TextField(
        verbose_name='Текст',
        help_text='Минимум два слова. Обязательно должно содержаться слово превосходно или роскошно',
        validators=[text_validation]
    )
    # Todo: Validator
    is_published = models.BooleanField(default=False)

    tags = models.ManyToManyField(
        verbose_name='Теги',
        to='Tag',
        related_name='items',
        on_delete=models.SET_NULL
    )
    category = models.ManyToManyField(
        verbose_name='Категория',
        to='Category',
        related_name='items',
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(Slug, Published):
    weight = models.PositiveSmallIntegerField(verbose_name='Вес', default=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(Slug, Published):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
