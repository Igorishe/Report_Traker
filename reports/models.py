from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Report(models.Model):
    class Statuses(models.TextChoices):
        NORMAL = 'Normal'
        CLOSED = 'Closed'
        URGENT = 'Urgent'
        FORGOTTEN = 'Forgotten'

    text = models.TextField(
        verbose_name='Текст',
        help_text='Пункт текста отчета'
    )
    date = models.DateTimeField(
        "date published",
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reports"
    )
    status = models.CharField(
        max_length=12,
        verbose_name='Status',
        choices=Statuses.choices,
        default=Statuses.NORMAL,
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.text[:10]
