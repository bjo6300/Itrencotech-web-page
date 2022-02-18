from django.contrib import admin

# Register your models here.
from itrencotech.models import Category, Portfolio, Order

admin.site.register(Portfolio)

admin.site.register(Order)