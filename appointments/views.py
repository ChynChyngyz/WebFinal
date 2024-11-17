from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment, Timetable
# from .forms import SpecialityForm
from .serializers import AppointmentSerializer, TimetableSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated


# Класс для списка специализаций
class AppointmentListView(APIView):
    """
    Класс для вывода списка записей к врачу.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Метод для получения списка записей к врачу.
        """
        specialities = Appointment.objects.all()  # Получаем все специализации
        serializer = AppointmentSerializer(specialities, many=True)  # Сериализуем данные
        return Response(serializer.data, status=status.HTTP_200_OK)


class AppointmentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request):
        """
        Метод для создания новой записи.
        """
        data = request.data
        serializer = AppointmentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def put(self, request, pk):
        """
        Метод для обновления записи.
        """
        try:
            speciality = Appointment.objects.get(pk=pk)  # Нахождение специализации
        except Appointment.DoesNotExist:
            return Response({"error": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(speciality, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def delete(self, request, pk):
        """
        Метод для удаления записей.
        """
        try:
            speciality = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(speciality, data=request.data, partial=True)
        speciality.delete()
        return Response({"message": "Appointment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class TimetableCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request):
        """
        Метод для создания рабочего дня.
        """
        data = request.data
        serializer = TimetableSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimetableListView(APIView):
    """
    Класс для вывода списка дней.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Метод для получения списка записей к врачу.
        """
        specialities = Timetable.objects.all()
        serializer = TimetableSerializer(specialities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TimetableUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def put(self, request, pk):
        """
        Метод для обновления записи.
        """
        try:
            speciality = Timetable.objects.get(pk=pk)  # Нахождение специализации
        except Timetable.DoesNotExist:
            return Response({"error": "Timetable not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TimetableSerializer(speciality, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimetableDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def delete(self, request, pk):
        """
        Метод для удаления записей.
        """
        try:
            speciality = Timetable.objects.get(pk=pk)
        except Timetable.DoesNotExist:
            return Response({"error": "Timetable not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TimetableSerializer(speciality, data=request.data, partial=True)
        speciality.delete()
        return Response({"message": "Timetable deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
