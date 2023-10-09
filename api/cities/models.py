from django.db import models
from api.common.models import SlugBaseModel
from django.utils.text import slugify


class City(SlugBaseModel):
    """Города"""
    slug = models.SlugField(unique=True, verbose_name="slug")
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
