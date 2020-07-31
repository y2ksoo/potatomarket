from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from wares import models as ware_model

class WareInlineAdmin(admin.TabularInline):
    model = ware_model.Ware

class CustomUserAdmin(admin.ModelAdmin):
    inlines = (WareInlineAdmin,)

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "trustseller",
    )

    list_filter = ("trustseller",) + UserAdmin.list_filter

admin.site.register(models.User, CustomUserAdmin)
