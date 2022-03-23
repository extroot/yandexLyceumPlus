# Generated by Django 3.2.12 on 2022-03-23 21:11

import catalog.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rating', '0001_initial'),
        ('catalog', '0004_auto_20220324_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ratings',
            field=models.ManyToManyField(related_name='items', through='rating.Rating', to=settings.AUTH_USER_MODEL, verbose_name='Оценки'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(help_text='Минимум два слова. Обязательно должно содержаться слово превосходно или роскошно', validators=[catalog.validators.text_validation], verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='catalog.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(related_name='items', to='catalog.Tag', verbose_name='Теги'),
        ),
    ]
