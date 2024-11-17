from rest_framework import serializers
from .models import Appointment, Timetable


class AppointmentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Appointment
    """
    class Meta:
        model = Appointment
        # указывается все поля модели, которые должны быть в JSON
        fields = '__all__'


class TimetableSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Timetable
    """
    class Meta:
        model = Timetable
        fields = '__all__'
