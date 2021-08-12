# Generated by Django 3.2.3 on 2021-08-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobinetReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Пункт отчета', verbose_name='Текст репорта')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.PositiveIntegerField(blank=True, verbose_name='Автор репорта')),
                ('author_name', models.CharField(blank=True, max_length=20, verbose_name='Логин автора')),
                ('status', models.CharField(choices=[('New', 'New'), ('Closed', 'Closed'), ('Actual', 'Actual')], default='New', max_length=12, verbose_name='Статус')),
                ('tag', models.CharField(choices=[('Normal', 'Normal'), ('Burning', 'Burning'), ('Forgotten', 'Forgotten'), ('Delayed', 'Delayed')], default='Normal', max_length=12, verbose_name='Тэг')),
            ],
            options={
                'verbose_name': 'Отчет MN',
                'verbose_name_plural': 'Отчеты MN',
            },
        ),
        migrations.CreateModel(
            name='MoneyBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Пункт отчета', verbose_name='Текст репорта')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.PositiveIntegerField(blank=True, verbose_name='Автор репорта')),
                ('author_name', models.CharField(blank=True, max_length=20, verbose_name='Логин автора')),
                ('status', models.CharField(choices=[('New', 'New'), ('Closed', 'Closed'), ('Actual', 'Actual')], default='New', max_length=12, verbose_name='Статус')),
                ('tag', models.CharField(choices=[('Normal', 'Normal'), ('Burning', 'Burning'), ('Forgotten', 'Forgotten'), ('Delayed', 'Delayed')], default='Normal', max_length=12, verbose_name='Тэг')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма возврата')),
                ('wallet', models.CharField(blank=True, max_length=50, verbose_name='Кошелек получателя')),
                ('link', models.CharField(max_length=50, verbose_name='Ссылка на пользователя')),
            ],
            options={
                'verbose_name': 'Возврат',
                'verbose_name_plural': 'Возвраты',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Пункт отчета', verbose_name='Текст репорта')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.PositiveIntegerField(blank=True, verbose_name='Автор репорта')),
                ('author_name', models.CharField(blank=True, max_length=20, verbose_name='Логин автора')),
                ('status', models.CharField(choices=[('New', 'New'), ('Closed', 'Closed'), ('Actual', 'Actual')], default='New', max_length=12, verbose_name='Статус')),
                ('tag', models.CharField(choices=[('Normal', 'Normal'), ('Burning', 'Burning'), ('Forgotten', 'Forgotten'), ('Delayed', 'Delayed')], default='Normal', max_length=12, verbose_name='Тэг')),
            ],
            options={
                'verbose_name': 'Отчет RS',
                'verbose_name_plural': 'Отчеты RS',
            },
        ),
    ]