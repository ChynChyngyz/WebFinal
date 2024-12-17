from rest_framework import serializers

from .models import Appointment, Timetable, ClinicTime, DoctorWorkingTime
from authUser.models import CustomUser

from service.serializers import ServiceSerializer
from authUser.serializers import UserSerializer, DoctorSerializer


class DoctorWorkingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorWorkingTime
        fields = ['time']


class AppointmentSerializer(serializers.ModelSerializer):

    service_details = ServiceSerializer(many=True, read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    user_details = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'date', 'time', 'price', 'status_of_appointment', 'date_created', 'user', 'doctor', 'doctor_details', 'service_details', 'user_details']


class TimetableSerializer(serializers.ModelSerializer):
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    doctor = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(role="Doctor"))

    time_work_0 = DoctorWorkingTimeSerializer(many=True, read_only=True)
    time_work_1 = DoctorWorkingTimeSerializer(many=True, read_only=True)
    time_work_2 = DoctorWorkingTimeSerializer(many=True, read_only=True)
    time_work_3 = DoctorWorkingTimeSerializer(many=True, read_only=True)
    time_work_4 = DoctorWorkingTimeSerializer(many=True, read_only=True)
    time_work_5 = DoctorWorkingTimeSerializer(many=True, read_only=True)
    time_work_6 = DoctorWorkingTimeSerializer(many=True, read_only=True)

    class Meta:
        model = Timetable
        fields = ['id', 'doctor', 'doctor_details', 'time_work_0', 'time_work_1', 'time_work_2', 'time_work_3',
                  'time_work_4', 'time_work_5', 'time_work_6']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        timetable = Timetable.objects.prefetch_related(
            'doctor_work_time'
        ).get(id=instance.id)
        time_work_dict = {
            0: "time_work_0",
            1: "time_work_1",
            2: "time_work_2",
            3: "time_work_3",
            4: "time_work_4",
            5: "time_work_5",
            6: "time_work_6",
        }

        for i in range(7):
            time_work_entries = timetable.doctor_work_time.filter(timetable__day_of_visit=i)
            data[time_work_dict[i]] = [entry.time for entry in time_work_entries]
            if not data[time_work_dict[i]]:
                del data[time_work_dict[i]]

        return data


class ClinicTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicTime
        fields = ['work_start_time', 'work_end_time', 'lunch_start_time', 'lunch_end_time', 'break_start_time', 'break_end_time']
