# Generated by Django 3.2.3 on 2021-08-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20210818_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobinetreport',
            name='last_edit',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='moneyback',
            name='last_edit',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='report',
            name='last_edit',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего изменения'),
        ),
    ]
