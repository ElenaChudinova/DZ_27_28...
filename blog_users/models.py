from django.contrib.auth.models import AbstractUser
from django.db import models


class BlogUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        verbose_name="Имя пользователя",
        help_text="Введите имя пользователя", null=True, blank=True
    )
    email = models.EmailField(unique=True, verbose_name="Email")

    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    avatar = models.ImageField(
        upload_to="photos",
        verbose_name="Аватар",
        null=True,
        blank=True,
        help_text="Загрузите изображение",
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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
