from django.apps import AppConfig


class DoctorsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api.doctors"

    verbose_name = 'Доктора'
