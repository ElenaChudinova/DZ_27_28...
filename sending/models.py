from django.contrib.auth.models import AbstractUser
from django.db import models


class MailingRecipient(AbstractUser):
    email = models.CharField(max_length=100, verbose_name="Email_mailing_recipient", unique=True)
    user_id = models.AutoField(
        auto_created=True, primary_key=True, verbose_name="ID Пользователя"
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

    def __str__(self):
        return f"{self.email} {self.comment}"

    class Meta:
        verbose_name = "получатель"
        verbose_name_plural = "получатели"


class Message(models.Model):
    message_id = models.AutoField(
        auto_created=True, primary_key=True, verbose_name="ID Сообщения пользователя"
    )
    subject_letter = models.CharField(
        max_length=100,
        verbose_name="Тема письма",
        help_text="Введите тему",
        null=True,
        blank=True,
    )
    letter = models.TextField(
        max_length=300,
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
        related_name='user',
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


class Newsletter(models.Model):
    CREATED = "Создана"
    LAUNCHED = "Запущена"
    COMPLETED = "Завершена"
    STATUS_MAILING = [
        (CREATED, "Создана"),
        (LAUNCHED, "Запущена"),
        (COMPLETED, "Завершена"),
    ]
    newsletter_id = models.AutoField(
        auto_created=True, primary_key=True, verbose_name="ID Рассылки"
    )
    first_shipment = models.DateTimeField(
        editable=False,
        auto_now_add=True,
        max_length=10,
        verbose_name="Дата и время первой отправки",
    )
    end_shipment = models.DateTimeField(
        editable=False,
        max_length=10,
        verbose_name="Дата и время окончания отправки",
    )
    status_news_letter = models.CharField(
        max_length=100,
        choices=STATUS_MAILING,
        default=CREATED,
        verbose_name="Статус",
    )
    message = models.ForeignKey(
        Message,
        related_name="comments",
        max_length=100,
        verbose_name="Сообщение",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    recipients = models.ManyToManyField(
        MailingRecipient, related_name="emails", verbose_name="Получатель"
    )

    disabling_mailings = models.BooleanField(default=False)

    def __str__(self):
        return self.status_news_letter

    class Meta:
        verbose_name = "статус"
        verbose_name_plural = "статусы"
        ordering = [
            "disabling_mailings",
        ]
        permissions = [
            ("can_edit_disabling_mailings", "Сan edit disabling mailings"),
        ]


class MailingAttempt(models.Model):
    Successfully = "Успешно"
    Not_successful = "Не успешно"
    STATUS_MAILING_ATTEMPT = [
        (Successfully, "Успешно"),
        (Not_successful, "Не успешно"),]

    date_attempt = models.DateTimeField(
        editable=False,
        auto_now=True,
        max_length=10,
        verbose_name="Дата и время попытки отправки рассылки",
    )
    status_mailing_attempt = models.CharField(
        max_length=50,
        choices=STATUS_MAILING_ATTEMPT,
        verbose_name="Статус рассылки",
    )
    mail_server_response = models.TextField(
        max_length=200, verbose_name="Ответ почтового сервера"
    )
    news_letter = models.ForeignKey(
        Newsletter,
        related_name='newsletter',
        verbose_name="Рассылка",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.status_mailing_attempt} {self.date_attempt}"

    class Meta:
        verbose_name = "статус"
        verbose_name_plural = "статусы"
