from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import CustomUser, Profile


class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Профиль'
    verbose_name_plural = 'Профили'


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )
    ordering = ('email', )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')


# admin.site.unregister(User)
# admin.site.register(CustomUser)
admin.site.register(CustomUser, UserAdmin)
