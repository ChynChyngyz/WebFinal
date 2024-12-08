from rest_framework import serializers
from .models import Appointment, Timetable
from authUser.models import CustomUser

from authUser.serializers import UserSerializer, DoctorSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Appointment
    """
    doctor = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(role='Doctor'), write_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(role='User'), write_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    user_details = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'date', 'time', 'price', 'status_of_appointment', 'date_created', 'doctor', 'doctor_details', 'user', 'user_details']


class TimetableSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Timetable
    """
    doctor_details = DoctorSerializer(source='doctor', many=True, read_only=True)

    class Meta:
        model = Timetable
        fields = ['id', 'day_of_visit', 'doctor_details']