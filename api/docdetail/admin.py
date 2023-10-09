from django.contrib import admin
from api.docdetail import models


@admin.register(models.Experience)
class ExperienceTranslationAdmin(admin.ModelAdmin):
    list_display = ("id", "doctor", "title", "year", "is_deleted")
    list_filter = ("title", "year")
    search_fields = ("year", "title")
    list_display_links = ("id",)


@admin.register(models.Certificates)
class CertificatesAdmin(admin.ModelAdmin):
    list_display = ("id", "doctor", "title", "year", "is_deleted")
    list_filter = ("title", "year")
    search_fields = ("title", "year")
    list_display_links = ("id",)


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("id", "doctor", "title", "year", "is_deleted")
    list_filter = ("title", "specialization", "year")
    search_fields = ("title", "specialization")
    list_display_links = ("id",)


@admin.register(models.Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("id", "doctor", "title", "is_deleted")
    list_filter = ("title",)
    search_fields = ("title", "id",)
    list_display_links = ("id",)
