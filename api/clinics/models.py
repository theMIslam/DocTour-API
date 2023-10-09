from django.db import models
from django.utils.safestring import mark_safe
from api.cities.models import City
from api.doctors.validators import PhoneValidator
from api.common.models import BaseModel


class Clinics(BaseModel):
    """Клиники"""
    title = models.CharField(max_length=150, verbose_name="Название")
    descriptions = models.CharField(max_length=300, verbose_name="Описание")
    photo = models.ImageField(
        upload_to="photos/",
        blank=True,
        verbose_name="Фото клиники",
        default="/default_photo/Hospital.webp",
    )
    address = models.CharField(max_length=150, verbose_name="Адрес", help_text="Текст")
    city = models.ForeignKey(
        to=City,
        on_delete=models.PROTECT,
        verbose_name="Город",
    )
    link_clinic = models.URLField(verbose_name="Ссылка на клинику", blank=True)
    link_2gis = models.URLField(verbose_name="Ссылка на 2GIS", blank=True)
    starting_working_day = models.TimeField(
        verbose_name="Начало рабочего времени", default="09:00"
    )
    contacts1 = models.CharField(
        verbose_name="Номер телефона 1",
        validators=[PhoneValidator],
        max_length=20,
        help_text="996 Whats-App",
    )
    contacts2 = models.CharField(
        verbose_name="Номер телефона 2",
        validators=[PhoneValidator],
        max_length=20,
        help_text="996",
        blank=True,
    )
    ending_working_day = models.TimeField(
        verbose_name="Конец рабочего времени", default="17:00"
    )
    weekday = models.CharField(
        max_length=50, verbose_name="Рабочие дни", help_text="пн-пт", default="пн-пт"
    )
    weekend = models.CharField(
        max_length=50, verbose_name="Выходные дни", help_text="сб-вс", default="сб-вс"
    )

    def image_img(self):
        if self.photo:
            return mark_safe(
                '<a href="{0}" target="_blank"><img src="{0}" width="50"/></a>'.format(
                    self.photo.url
                )
            )
        else:
            return mark_safe(
                '<a href="{0}" target="_blank"><img src="{0}" width="50"/></a>'.format(
                    "/back_media/default_photo/Hospital.webp"
                )
            )

    def __str__(self):
        return self.title

    image_img.short_description = "Фото клиники"
    image_img.allow_tags = True


    class Meta:
        verbose_name = "Клиника"
        verbose_name_plural = "Клиники"
