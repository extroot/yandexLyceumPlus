# Generated by Django 3.2.12 on 2022-04-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=128, verbose_name='Имя'),
            preserve_default=False,
        ),
    ]
