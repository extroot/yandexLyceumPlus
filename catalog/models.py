from django.db import models

from catalog.validators import text_validation
from core.models import Published, Slug


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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(Slug, Published):
    weight = models.PositiveSmallIntegerField(verbose_name='Вес', default=100)
    name = models.CharField(verbose_name='Имя', max_length=128)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(Slug, Published):
    name = models.CharField(verbose_name='Имя', max_length=128)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
