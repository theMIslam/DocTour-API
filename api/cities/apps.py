from django.apps import AppConfig


class CityConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api.cities"

    verbose_name = 'Города'
