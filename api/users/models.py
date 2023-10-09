from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from api.doctors.constants import GENDER
from api.doctors.validators import PhoneValidator
from api.users.managers import UserManager
from api.common.models import BaseModel



class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    fullname = models.CharField("Фио", max_length=100)
    phone_number = models.CharField(
        "Телефон", validators=[PhoneValidator], unique=True, max_length=300
    )
    gender = models.CharField("Пол", max_length=20, choices=GENDER)
    birthday = models.DateField("День рождения", blank=True, null=True)

    is_active = models.BooleanField("Активен", default=True)
    is_staff = models.BooleanField("Персонал", default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []  # Необязательные поля для создания суперпользователя

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.fullname}, {self.phone_number}"


class UserConfirm(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users_code')
    code = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.user}, {self.code}"

class PasswordResetToken(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.user}, {self.token}"

