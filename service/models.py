from django.db import models
from speciality.models import Speciality
from authUser.models import CustomUser  # CustomUserManager


class Service(models.Model):
    """
    Класс модели услуга.
    """
    DoesNotExist = None
    objects = None

    title = models.CharField(max_length=100, verbose_name='Название услуги')
    doctor = models.ForeignKey(CustomUser, verbose_name='Доктор', on_delete=models.CASCADE,
                               related_name='services')
    image = models.ImageField(upload_to='image_service/', verbose_name='Изображение', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='Цена услуги')
    speciality = models.ForeignKey(Speciality, on_delete=models.SET_NULL, verbose_name='Специализация', blank=True,
                                   null=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
