import datetime

from datetime import timedelta
from web import settings
from django.core.mail import send_mail

from .models import Appointment, Timetable, ClinicTime


def send_email_for_patient(email, appointment: Appointment):
    # service_name = appointment.service if appointment.service else 'Не указана'

    send_mail(
        'Запись на прием',
        f'Вы записаны на прием к врачу: {appointment.doctor}\n'
        f'Дата: {appointment.date}\n'
        f'Время: {appointment.time}\n'
        f'Услуга: {appointment.time}\n'
        f'Цена: {appointment.price} сом\n',
        settings.EMAIL_HOST_USER,
        [email]
    )

def send_email_for_patient_update(email, appointment: Appointment):

    send_mail(
        'Изменения в записи на прием',
        f'Внесены изменения в записи на прием к врачу: {appointment.doctor}\n'
        f'Дата: {appointment.date}\n'
        f' Время: {appointment.time}\n'
        f'Услуга: {appointment.service}\n',
        settings.EMAIL_HOST_USER,
        [email]
    )


def days_of_week(date):
    days_of_week = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье",
    }

    if isinstance(date, str):
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    day_of_week = date.weekday()

    return days_of_week[day_of_week]


def is_valid_appointment_time(appointment_time, doctor, appointment_date):
    errors = []

    day_of_week = appointment_date.weekday()
    today = datetime.datetime.today().date()

    timetable = Timetable.objects.filter(doctor=doctor, day_of_visit=day_of_week).first()

    if not timetable:
        errors.append(f"В выбранный день врач {doctor} не принимает пациентов.")
        return errors

    clinic_time = ClinicTime.objects.first()

    if not clinic_time:
        errors.append("Не настроены часы работы клиники.")
        return errors

    if isinstance(appointment_time, str):
        appointment_time = datetime.datetime.strptime(appointment_time, "%H:%M").time()

    if appointment_date < today:
        errors.append(f"Выберите не прошедшие дни дату")

    if not (clinic_time.work_start_time <= appointment_time <= clinic_time.work_end_time):
        errors.append(f"В выбранное время клиника не работает.")

    elif clinic_time.lunch_start_time <= appointment_time < clinic_time.lunch_end_time:
        errors.append("Выбранное время попадает в обеденный перерыв.")

    elif clinic_time.break_start_time <= appointment_time < clinic_time.break_end_time:
        errors.append("Выбранное время попадает в полдник.")

    existing_appointments = Appointment.objects.filter(
        doctor=doctor,
        date=appointment_date,
        time=appointment_time,
        status_of_appointment__in=['WAITING', 'CONFIRMED']
    )

    if existing_appointments.exists():
        errors.append(f"Врач {doctor} уже занят в выбранное время: {appointment_time}.")

    doctor_work_times = timetable.doctor_work_time.all()

    valid_time_found = False

    for doctor_work_time in doctor_work_times:
        doctor_work_time_str = doctor_work_time.time if isinstance(doctor_work_time.time,
                                                                   str) else doctor_work_time.time.strftime('%H:%M')

        doctor_work_time_obj = datetime.datetime.strptime(doctor_work_time_str, "%H:%M").time()

        if doctor_work_time_obj == appointment_time:
            valid_time_found = True
            break

    if not valid_time_found:
        errors.append(f"Врач {doctor} не работает в это время: {appointment_time}.")

    return errors
