from django.db import models

# from services.models import Service
from authUser.models import CustomUser


class Appointment(models.Model):
    """
    Класс модели запись на обследование.
    """

    DoesNotExist = None
    objects = None

    WAITING = 'WAITING'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = [
        (WAITING, 'ожидание приема'),
        (COMPLETED, 'прием оказан'),
        (CANCELLED, 'прием отменен'),
    ]

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='пациент',
        related_name='appointments_as_user'
    )

    doctor = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        verbose_name='врач',
        related_name='appointments_as_doctor',
        null=True
    )

    # service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='услуга')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    status_of_appointment = models.CharField(max_length=20, choices=STATUS_CHOICES, default=WAITING)
    doctor_id = models.ManyToManyField(CustomUser, verbose_name='Доктор', limit_choices_to={'role': 'Doctor'},
                                       related_name='appointments')
    date_created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(verbose_name='Цена')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.service = None

    def __str__(self):
        return f'{self.service} ({self.doctor}): ({self.status_of_appointment}) - {self.user}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def delete(self, *args, **kwargs):
        self.status_of_appointment = 'CANCELLED'
        self.save()
        super().delete(*args, **kwargs)


class Timetable(models.Model):
    """
    Класс для расписания.
    """
    DoesNotExist = None
    objects = None

    DAYS_OF_WEEK = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    doctor = models.ManyToManyField(CustomUser, verbose_name='Врач')
    day_of_visit = models.PositiveSmallIntegerField(choices=DAYS_OF_WEEK, unique=True, verbose_name='День приема')

    def __str__(self):
        return f'{self.day_of_visit} {self.doctor}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
