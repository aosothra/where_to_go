# Generated by Django 4.0.4 on 2022-05-03 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_image_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='index',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Приоритет при отображении'),
        ),
    ]