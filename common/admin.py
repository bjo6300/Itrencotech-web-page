from django.contrib import admin
from .models import Users


# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password', 'phone_num', 'company_name',
                    'company_address', 'company_tel', 'email', 'register_date')


admin.site.unregister(Users)
admin.site.register(Users, UserAdmin)
