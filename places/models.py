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


class Image(models.Model):
    
    image_file = models.ImageField(
        'Изображение'
    )

    index = models.PositiveIntegerField(
        verbose_name='Приоритет при отображении',
        default=0
    )

    place = models.ForeignKey(
        Place,
        on_delete=models.DO_NOTHING,
        verbose_name='Место',
        related_name='images'
    )


    def __str__(self) -> str:
        return f'{self.index}-{self.place.title}'
