import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("ID"),
    )
    is_deleted = models.BooleanField(default=False, verbose_name=_("удаленный?"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("дата изменения"))

    class Meta:
        abstract = True


class SlugBaseModel(models.Model):
    slug = models.SlugField(unique=True, verbose_name="slug", primary_key=True)
    is_deleted = models.BooleanField(default=False, verbose_name=_("удаленный?"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("дата изменения"))

    class Meta:
        abstract = True
