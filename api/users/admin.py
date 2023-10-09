from django.contrib import admin
from .models import User
from api.doctors import models


class FavoriteDoctorsInline(admin.TabularInline):
    model = models.FavoriteDoctors


class FavoriteClinicsInline(admin.TabularInline):
    model = models.FavoriteClinics


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "fullname", "gender", "phone_number")
    list_display_links = ("id", "fullname")
    list_filter = ("gender", "is_active", "is_staff")
    search_fields = ("fullname", "phone_number")
    inlines = (FavoriteClinicsInline, FavoriteDoctorsInline)


