from django.contrib.auth.models import AbstractUser
from django.db import models


class MailingRecipient(AbstractUser):
    email = models.CharField(max_length=50, verbose_name="Email", unique=True)
    user_id = models.AutoField(
        auto_created=True, primary_key=True, verbose_name="ID Клиента"
    )
    username = models.CharField(
        max_length=150,
        verbose_name="Ф.И.О.",
        help_text="Введите ваши инициалы",
        null=True,
        blank=True,
    )
    comment = models.TextField(
        max_length=1000,
        verbose_name="Комментарий",
        help_text="Введите комментарии",
        null=True,
        blank=True,
    )

    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

