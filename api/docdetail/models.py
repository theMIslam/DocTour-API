from django.db import models
from api.common.models import BaseModel
from api.doctors.models import Doctor


class Certificates(BaseModel):
    """Сертификаты доктора"""

    title = models.TextField(verbose_name="Место получения")
    doctor = models.ForeignKey(
        to=Doctor,
        on_delete=models.CASCADE,
        related_name="doctor_certificates",
        verbose_name="Доктор",
    )
    year = models.CharField(
        max_length=50, verbose_name="Год получения сертификата", help_text="1990 2000"
    )

    def __str__(self):
        return f"{self.year} -> {self.title}"

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"


class Experience(BaseModel):
    """Опыт работы доктора"""

    title = models.TextField(verbose_name="Место работы")
    doctor = models.ForeignKey(
        to=Doctor,
        related_name="doctor_experience",
        on_delete=models.CASCADE,
        verbose_name="Доктор",
    )
    year = models.CharField(
        max_length=50, verbose_name="Период работы |года", help_text="1990 2000"
    )

    def __str__(self):
        return f"{self.year} -> {self.title}"

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"


class Education(BaseModel):
    """Образование доктора"""

    title = models.TextField(verbose_name="Учебное заведение")
    specialization = models.CharField(max_length=150, verbose_name="Специализация")
    doctor = models.ForeignKey(
        to=Doctor,
        related_name="doctor_education",
        on_delete=models.CASCADE,
        verbose_name="Доктор",
    )
    year = models.CharField(
        max_length=50, verbose_name="Период учебы |года", help_text="1990 2000"
    )

    def __str__(self):
        return f"{self.title} -> {self.year} -> {self.specialization}"

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образования"


class Specialization(BaseModel):
    """Специализации доктора"""

    title = models.CharField(max_length=150, verbose_name="Название")
    doctor = models.ForeignKey(
        to=Doctor,
        related_name="doctor_specialization",
        on_delete=models.CASCADE,
        verbose_name="Доктор",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"
