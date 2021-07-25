from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Customer, CustomUser


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = (
        "first_name", "last_name", "email", "gender",  "company", "city", "title", "latitude", "longitude",
    )
    list_display = (
        "first_name", "last_name", "email", "gender",  "company", "city", "title", "latitude", "longitude",
    )
