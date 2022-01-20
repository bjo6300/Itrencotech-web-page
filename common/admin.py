from django.contrib import admin
from .models import UserModel
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('user_name', 'user_id', 'password1', 'phone_num',
#                     'company_name', 'company_address', 'company_tel', 'email')  # User 클래스의 변수 이름과 통일해야 함
# admin.site.register(UserModel, UserAdmin)  # site에 등록


class UserAdmin(BaseUserAdmin):
    # 사용자 변경 및 추가 Form을 Custom한 거로 결정
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('user_id', 'user_name', 'phone_num', 'company_name',
                    'company_address', 'company_tel', 'email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('user_id', 'password')}),
        ('Personal info', {'fields': ('user_name', 'phone_num',
                                      'company_name', 'company_address',
                                      'company_tel', 'email',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'user_name', 'phone_num', 'company_name',
                       'company_address', 'company_tel', 'email', 'password')}
         ),
    )
    search_fields = ('user_id',)
    ordering = ('user_id',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

