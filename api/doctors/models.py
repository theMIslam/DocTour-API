from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from api.doctors import validators, constants
from api.clinics.models import Clinics
from api.users.models import User
from api.common.models import BaseModel, SlugBaseModel
from api.cities.models import City


class Speciality(SlugBaseModel):
    """Специальности"""
    slug = models.SlugField(unique=True, verbose_name="slug")
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Service(SlugBaseModel):
    slug = models.SlugField(unique=True, verbose_name="slug")
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class SubService(SlugBaseModel):
    """Под Услуги"""
    slug = models.SlugField(unique=True, verbose_name="slug")
    name = models.CharField(max_length=100, verbose_name="Название")
    service = models.ForeignKey(
        to=Service,
        on_delete=models.CASCADE,
        related_name="subservice_service",
        verbose_name="Услуги",
    )
    clinic = models.ManyToManyField(
        Clinics, related_name="subservice_clinic", verbose_name="Клиники"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Под услуга"
        verbose_name_plural = "Под услуги"

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Doctor(BaseModel):
    """Доктора"""

    photo = models.ImageField(
        upload_to="photos/",
        blank=True,
        verbose_name="Фото профиля",
        default="/default_photo/men.png",
    )
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    specialties = models.ManyToManyField(
        Speciality, related_name="doctors_specialties", verbose_name="Специальность"
    )
    experience = models.PositiveSmallIntegerField(
        verbose_name="Опыт работы", help_text="Сколько лет"
    )
    instagram = models.URLField("Ссылка на instagram", blank=True)
    clinic = models.ManyToManyField(
        Clinics, related_name="doctor_clinics", verbose_name="Клиника", blank=True
    )
    price = models.PositiveSmallIntegerField(
        verbose_name="Цена за прием", help_text="Прием от: "
    )
    summary = models.CharField(
        max_length=1000, null=True, verbose_name="Краткое описание"
    )
    category_services = models.ManyToManyField(
        Service,
        related_name="doctor_services",
        verbose_name="Услуги",
        blank=True,
    )
    city = models.ForeignKey(
        to=City,
        related_name="doctor_city",
        on_delete=models.PROTECT,
        verbose_name="Город",
    )
    phone = models.CharField(
        verbose_name="Телефон",
        validators=[validators.PhoneValidator],
        max_length=20,
        help_text="996 Whats-App",
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

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
                    "/media/default_photo/men.png"
                )
            )

    image_img.short_description = "Фото профиля"
    image_img.allow_tags = True



class Review(BaseModel):
    """Отзывы"""

    text = models.TextField(verbose_name="Текст")
    stars = models.IntegerField(choices=constants.review_stars, verbose_name="Звёзды")
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="doctor_reviews",
        verbose_name="Доктор",
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"



class FavoriteDoctors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class FavoriteClinics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinics = models.ForeignKey(Clinics, on_delete=models.CASCADE)
