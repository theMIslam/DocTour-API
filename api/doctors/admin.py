from django.contrib import admin
from api.doctors import models


class FavoriteDoctors(admin.TabularInline):
    model = models.FavoriteDoctors


class FavoriteClinics(admin.TabularInline):
    model = models.FavoriteClinics


@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "city", "image_img", "is_deleted")
    list_filter = ("full_name", "experience", "city", "price")
    search_fields = ("full_name", "experience", "price")
    list_display_links = ("id",)
    list_editable = ('is_deleted',)


@admin.register(models.Speciality)
class SpecialityAdmin(admin.ModelAdmin):
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


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
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


@admin.register(models.SubService)
class SubServiceAdmin(admin.ModelAdmin):
    list_display = ("slug", "name", "service", "is_deleted")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "slug",
                    "service",
                    "clinic",
                    "is_deleted",
                )
            },
        ),
    )
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class ReviewPermissions(admin.ModelAdmin):
    """ Запрет на Post и Put для Review """

    def has_add_permission(self, request):
        return False  # Запретить добавление новых записей

    def has_change_permission(self, request, obj=None):
        return False  # Запретить изменение существующих записей


@admin.register(models.Review)
class ReviewAdmin(ReviewPermissions):
    list_display = ("id", "text", "stars", "created_at", "user", "is_deleted",)
    list_filter = ("stars",)
    search_fields = ("text",)
    list_display_links = ("id", "text", "stars", "created_at", "user")
