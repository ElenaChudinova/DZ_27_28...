from django.db import models

from users.models import MailingRecipient


class Message(models.Model):
    message_id = models.AutoField(
        auto_created=True, primary_key=True, verbose_name="ID Сообщения"
    )
    subject_letter = models.CharField(
        max_length=100,
        verbose_name="Тема письма",
        help_text="Введите тему",
        null=True,
        blank=True,
    )
    letter = models.TextField(
        max_length=20000,
        verbose_name="Текст письма",
        help_text="Введите текст",
        null=True,
        blank=True,
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    owner = models.ForeignKey(
        MailingRecipient,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="Владелец",
        help_text="Укажите автора письма",
    )

    def __str__(self):
        return f"{self.subject_letter} {self.letter}"

    class Meta:
        verbose_name = "письмо"
        verbose_name_plural = "письма"
        ordering = [
            "letter",
        ]
        permissions = [
            ("can_edit_subject_letter", "Can edit subject_letter"),
            ("can_edit_letter", "Can edit letter"),
        ]

