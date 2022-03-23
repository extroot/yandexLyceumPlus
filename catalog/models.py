from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'
