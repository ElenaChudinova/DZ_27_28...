from django.contrib.auth.models import AbstractUser
from django.db import models


class Clients(AbstractUser):
    email = models.CharField(max_length=50, verbose_name="Email", unique=True)
    сlient_id = models.AutoField(
        auto_created=True, primary_key=True, verbose_name="ID Клиента"
    )
    сlient_name = models.CharField(
        max_length=150,
        verbose_name="Ф.И.О.",
        help_text="Введите ваши инициалы",
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Страна",
        blank=True,
        null=True,
        help_text="Введите Страну",
    )
    token = models.CharField(
            max_length=100, verbose_name="Token", blank=True, null=True
        )

    CLIENT_NAME_FIELD = "email"
    REQUIRED_FIELDS = ["client_name"]


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

