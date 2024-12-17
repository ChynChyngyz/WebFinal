from django.contrib import admin

from .models import Appointment, Timetable, ClinicTime, DoctorWorkingTime, AppointmentTime


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = ('user', 'doctor', 'status_of_appointment',)


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'get_doctor_work_times', 'day_of_visit')

    def get_doctor_work_times(self, obj):
        return ", ".join([str(time) for time in obj.doctor_work_time.all()])
    get_doctor_work_times.short_description = 'Часы работы врача'

    list_filter = ('day_of_visit',)

    filter_horizontal = ('doctor_work_time',)


@admin.register(ClinicTime)
class ClinicTimeAdmin(admin.ModelAdmin):
    list_display = (
        'work_start_time',
        'work_end_time',
        'lunch_start_time',
        'lunch_end_time',
        'break_start_time',
        'break_end_time'
    )

    list_filter = ('work_start_time', 'work_end_time')

    ordering = ['work_start_time']

    fieldsets = (
        (None, {
            'fields': (
                'work_start_time',
                'work_end_time',
                'lunch_start_time',
                'lunch_end_time',
                'break_start_time',
                'break_end_time'
            )
        }),
    )


@admin.register(DoctorWorkingTime)
class DoctorWorkingTimeAdmin(admin.ModelAdmin):

    list_display = ['time']


@admin.register(AppointmentTime)
class AppointmentTimeAdmin(admin.ModelAdmin):

    list_display = ['appointment_time']