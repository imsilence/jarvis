#encoding: utf-8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import UserCreationForm, UserChangeForm
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'nickname', 'password')}),
        (_('account.admin.user.contants'), {'fields': ('email', 'telephone')}),
        (_('account.admin.user.permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('account.admin.user.dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'nickname', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'nickname', 'email', 'telephone', 'is_staff',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', )
    search_fields = ('username', 'nickname', 'email', 'telephone', )
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)