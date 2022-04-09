from catalog.models import Category, Item, Tag

from django.contrib import admin


admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'text')
    list_display_links = ('name', 'text')
    list_editable = ('is_published',)
    filter_horizontal = ('tags',)
