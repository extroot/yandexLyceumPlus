from django.db import models


class Published(models.Model):
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)

    class Meta:
        abstract = True


class Slug(models.Model):
    slug = models.SlugField(verbose_name='Slug', unique=True, max_length=200)

    class Meta:
        abstract = True
