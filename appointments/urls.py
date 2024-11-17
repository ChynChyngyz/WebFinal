from django.urls import path

from appointments.apps import AppointmentsConfig
from appointments.views import (AppointmentCreateView, AppointmentListView, AppointmentUpdateView, AppointmentDeleteView,
                                TimetableListView, TimetableCreateView, TimetableUpdateView, TimetableDeleteView)

app_name = AppointmentsConfig.name

urlpatterns = [
    path('appointment-list', AppointmentListView.as_view(), name='appointment_list'),
    path('create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('update/<int:pk>/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('delete/<int:pk>/', AppointmentDeleteView.as_view(), name='appointment_update'),
    path('timetable/', TimetableListView.as_view(), name='timetable_list'),
    path('timetable/create/', TimetableCreateView.as_view(), name='timetable_create'),
    path('timetable/update/<int:pk>/', TimetableUpdateView.as_view(), name='timetable_list'),
    path('timetable/delete/<int:pk>/', TimetableDeleteView.as_view(), name='timetable_list')
]
