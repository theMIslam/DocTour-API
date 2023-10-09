from django.contrib import admin
from api.cities import models


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("slug", "name", "is_deleted")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "slug",
                    "is_deleted",
                )
            },
        ),
    )
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    # list_display_links = ("slug", "name",)
