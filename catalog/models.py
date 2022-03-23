from django.db import models

from core.models import Published


class Item(Published):
    name = models.CharField(max_length=150)
    text = models.TextField(
        verbose_name='Текст',
        help_text='Минимум два слова. Обязательно должно содержаться слово превосходно или роскошно'
    )
    # Todo: Validator
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
