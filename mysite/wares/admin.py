from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = (
        "name", "used_by",
    )

    def used_by(self, obj):
        return obj.ware.count()


@admin.register(models.Ware)
class WareAdmin(admin.ModelAdmin):

    list_display = (
        "name", "price", "city", "seller",
    )

    list_filter = (
        "category", "city",
    )

    search_fields = (
        "name",
    )
    