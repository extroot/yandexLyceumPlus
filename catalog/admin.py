from catalog.models import Category, Image, Item, Tag

from django.contrib import admin


admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'text', 'image_tmb')
    list_display_links = ('name', 'text')
    list_editable = ('is_published',)
    filter_horizontal = ('tags',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'item')
