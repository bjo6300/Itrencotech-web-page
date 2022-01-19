from django.contrib import admin
from .models import UserModel

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_id', 'password1', 'phone_num',
                    'company_name', 'company_address', 'company_tel', 'email')  # User 클래스의 변수 이름과 통일해야 함


admin.site.register(UserModel, UserAdmin)  # site에 등록
