from rest_framework import serializers
from .models import Appointment, Timetable
from authUser.models import CustomUser
from drf_spectacular.utils import extend_schema_field


class DoctorForAppointSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'nickname', 'speciality', 'education', 'description']


class AppointmentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Appointment
    """
    doctor = DoctorForAppointSerializer(many=True, read_only=True)
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(role='Doctor'), many=True)

    class Meta:
        model = Appointment
        fields = ['id', 'date', 'time', 'doctor', 'doctor_id', 'price', 'status_of_appointment', 'date_created']


class TimetableSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Timetable
    """
    class Meta:
        model = Timetable
        fields = '__all__'
