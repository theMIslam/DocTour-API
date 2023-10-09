from django.contrib import admin
from api.clinics import models


@admin.register(models.Clinics)
class ClinicsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "address",
        "contacts1",
        "weekday",
        "weekend",
        "image_img",
    )
    list_filter = ("title", "address")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "photo",
                    "title",
                    "city",
                    "address",
                    "descriptions",
                    "starting_working_day",
                    "ending_working_day",
                    "link_clinic",
                    "link_2gis",
                    "contacts1",
                    "contacts2",
                    "weekday",
                    "weekend",
                )
            },
        ),
    )
    search_fields = ("title", "address", "contacts")
    list_display_links = ("id",)
