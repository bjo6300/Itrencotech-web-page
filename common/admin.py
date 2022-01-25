"""
common/admin.py
"""

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('userid', 'username', 'phone_num', 'company_name',
                    'company_address', 'company_tel', 'email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('userid', 'password')}),
        ('Personal info', {'fields': ('username', 'phone_num', 'company_name',
                                      'company_address', 'company_tel', 'email')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('userid', 'username', 'phone_num', 'company_name',
                       'company_address', 'company_tel', 'email', 'password1', 'password2')}
         ),
    )
    search_fields = ('userid',)
    ordering = ('userid',)
    filter_horizontal = ()


# 생성한 Custom User Model과 관리자 Form을 사용하도록 등록
admin.site.register(User, UserAdmin)
# 기본적으로 제공되는 Django의 Group은 사용하지 않음
admin.site.unregister(Group)
