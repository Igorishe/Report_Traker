from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ParentReport(models.Model):
    class Statuses(models.TextChoices):
        NEW = 'New'
        CLOSED = 'Closed'
        ACTUAL = 'Actual'

    class Tags(models.TextChoices):
        NORMAL = 'Normal'
        BURNING = 'Burning'
        FORGOTTEN = 'Forgotten'
        DELAYED = 'Delayed'

    text = models.TextField(
        verbose_name='Текст репорта',
        help_text='Пункт отчета',
    )
    date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    author = models.PositiveIntegerField(
        verbose_name='Автор репорта',
        blank=True,
    )
    author_name = models.CharField(
        max_length=20,
        verbose_name='Логин автора',
        blank=True,
    )
    status = models.CharField(
        max_length=12,
        verbose_name='Статус',
        choices=Statuses.choices,
        default=Statuses.NEW,
    )
    tag = models.CharField(
        max_length=12,
        verbose_name='Тэг',
        choices=Tags.choices,
        default=Tags.NORMAL,
    )

    class Meta:
        abstract = True
        ordering = ['-date']

    def __str__(self):
        return self.text[:12]


class Report(ParentReport):
    class Meta:
        verbose_name = 'Отчет RS'
        verbose_name_plural = 'Отчеты RS'


class MobinetReport(ParentReport):
    class Meta:
        verbose_name = 'Отчет MN'
        verbose_name_plural = 'Отчеты MN'


class ParentMoneyback(ParentReport):
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма возврата',
    )
    wallet = models.CharField(
        max_length=50,
        verbose_name='Кошелек получателя',
        blank=True,
    )
    link = models.CharField(
        max_length=50,
        verbose_name='Ссылка на пользователя',
    )

    class Meta:
        abstract = True


class MoneyBack(ParentMoneyback):
    class Meta:
        verbose_name = 'Возврат'
        verbose_name_plural = 'Возвраты'
