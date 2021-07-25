from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from import_export.admin import ImportExportModelAdmin

from .models import Customer, CustomUser


@admin.register(Customer)
class CustomerResource(ImportExportModelAdmin):
    pass
