from django.db import models

class Category(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name="id")
    category_name = models.CharField(max_length=50, verbose_name="Наименование", help_text='Введите категорию')
    description = models.TextField(
        max_length=300, verbose_name="Описание", null=True, blank=True
    )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Blog(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name="id")
    blog_name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование заголовка",
    )
    description = models.TextField(
        max_length=1000, verbose_name="Содержимое", null=True, blank=True, help_text='Введите описание блога'
    )
    image = models.ImageField(
        upload_to="photos", verbose_name="Превью", null=True, blank=True
    )
    category_name = models.CharField(max_length=50, verbose_name="Категория", help_text='Введите категорию')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания", editable=False, blank=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
        editable=False,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blogs",
    )

    publication = models.BooleanField(default=False)

    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    def __str__(self):
        return f"{self.blog_name} {self.category_name}"

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = [
            "blog_name",
        ]
