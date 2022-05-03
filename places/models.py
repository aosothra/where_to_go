from django.db import models


class Place(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=200, 
        blank=False
    )

    description_short = models.CharField(
        verbose_name='Короткое описание',
        max_length=2000,
        blank=True
    )

    description_long = models.TextField(
        verbose_name='Полное описание',
        blank=True
    )

    lat = models.FloatField(
        verbose_name='Положение по широте'
    )

    lng = models.FloatField(
        verbose_name='Положение по долготе'
    )

    
    def __str__(self) -> str:
        return f'{self.title} ({self.lat}, {self.lng})'