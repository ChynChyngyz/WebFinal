from django.db import models
from django.utils.timezone import now

from authUser.models import CustomUser


class DoctorWorkingTime(models.Model):

    time = models.CharField(max_length=5, unique=True, verbose_name="Время")
    # doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Доктор")

    def __str__(self):
        return f'Часы работы доктора: {self.time}'

    class Meta:
        verbose_name = 'Часы работы доктора'
        verbose_name_plural = 'Часы работы докторов'


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('WAITING', 'Ожидание'),
        ('COMPLETED', 'Завершен'),
        ('CANCELLED', 'Отменен'),
        ('EXPIRED', 'Выгоревший'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments_as_user', verbose_name='Пользователь')
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments_as_doctor', verbose_name='Доктор')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    status_of_appointment = models.CharField(max_length=20, choices=STATUS_CHOICES, default='WAITING')
    date_created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return f'{self.doctor}: {self.date} - {self.time} ({self.status_of_appointment})'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Timetable(models.Model):
    DAYS_OF_WEEK = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Врач')
    doctor_work_time = models.ManyToManyField(DoctorWorkingTime, verbose_name='Часы работы врача')
    day_of_visit = models.PositiveSmallIntegerField(choices=DAYS_OF_WEEK, verbose_name='День приема')

    def __str__(self):
        return f'{self.day_of_visit} {self.doctor}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class ClinicTime(models.Model):

    work_start_time = models.TimeField(verbose_name='Начало рабочего дня')
    work_end_time = models.TimeField(verbose_name='Конец рабочего дня')

    lunch_start_time = models.TimeField(verbose_name='Начало обеда')
    lunch_end_time = models.TimeField(verbose_name='Конец обеда')

    break_start_time = models.TimeField(verbose_name='Начало полдника')
    break_end_time = models.TimeField(verbose_name='Конец полдника')

    def __str__(self):
        return f'Часы работы клиники: {self.work_start_time} - {self.work_end_time}'

    class Meta:
        verbose_name = 'Часы работы клиники'
        verbose_name_plural = 'Часы работы клиники'
