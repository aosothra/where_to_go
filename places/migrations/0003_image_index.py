# Generated by Django 3.2.13 on 2022-05-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='index',
            field=models.PositiveIntegerField(default=0, verbose_name='Приоритет при отображении'),
        ),
    ]