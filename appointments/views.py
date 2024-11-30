# from django.views.decorators.csrf import csrf_exempt

from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Appointment, Timetable

# from .forms import SpecialityForm

from .serializers import AppointmentSerializer, TimetableSerializer


# Класс для списка специализаций
class AppointmentListView(APIView):
    """
    Класс для вывода списка записей к врачу.
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        responses={200: AppointmentSerializer(many=True)},
    )
    def get(self, request):
        """
        Метод для получения списка записей к врачу.
        """
        specialities = Appointment.objects.all()  # Получаем все специализации
        serializer = AppointmentSerializer(specialities, many=True)  # Сериализуем данные
        return Response(serializer.data, status=status.HTTP_200_OK)


class AppointmentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=AppointmentSerializer,
        responses={201: {"message": "Appointment created successful"}},
    )
    def post(self, request):
        """
        Метод для создания новой записи.
        """
        if request.user.role != 'Admin':
            return Response({"error": "Access denied. Only admin can perform this action"},
                            status=status.HTTP_403_FORBIDDEN)

        data = request.data
        serializer = AppointmentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=AppointmentSerializer,
        responses={201: {"message": "Appointment updated successful"}},
    )
    def put(self, request, pk):
        """
        Метод для обновления записи.
        """
        if request.user.role != 'Admin':
            return Response({"error": "Access denied. Only admin can perform this action"},
                            status=status.HTTP_403_FORBIDDEN)

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

    @extend_schema(
        request=AppointmentSerializer,
        responses={204: {"message": "Appointment deleted successful"}},
    )
    def delete(self, request, pk):
        """
        Метод для удаления записей.
        """
        if request.user.role != 'Admin':
            return Response({"error": "Access denied. Only admin can perform this action"},
                            status=status.HTTP_403_FORBIDDEN)

        try:
            speciality = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(speciality, data=request.data, partial=True)
        speciality.delete()
        return Response({"message": "Appointment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class TimetableCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=AppointmentSerializer,
        responses={201: {"message": "Timetable created successful"}},
    )
    def post(self, request):
        """
        Метод для создания рабочего дня.
        """
        if request.user.role != 'Admin':
            return Response({"error": "Access denied. Only admin can perform this action"},
                            status=status.HTTP_403_FORBIDDEN)

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

    @extend_schema(
        request=None,
        responses={200: TimetableSerializer(many=True)},
    )
    def get(self, request):
        """
        Метод для получения списка записей к врачу.
        """
        specialities = Timetable.objects.all()
        serializer = TimetableSerializer(specialities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TimetableUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=AppointmentSerializer,
        responses={201: {"message": "Timetable updated successful"}},
    )
    def put(self, request, pk):
        """
        Метод для обновления дней.
        """
        if request.user.role != 'Admin':
            return Response({"error": "Access denied. Only admin can perform this action"},
                            status=status.HTTP_403_FORBIDDEN)

        try:
            speciality = Timetable.objects.get(pk=pk)
        except Timetable.DoesNotExist:
            return Response({"error": "Timetable not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TimetableSerializer(speciality, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimetableDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=AppointmentSerializer,
        responses={204: {"message": "Timetable deleted successful"}},
    )
    def delete(self, request, pk):
        """
        Метод для удаления дней.
        """
        if request.user.role != 'Admin':
            return Response({"error": "Access denied. Only admin can perform this action"},
                            status=status.HTTP_403_FORBIDDEN)

        try:
            speciality = Timetable.objects.get(pk=pk)
        except Timetable.DoesNotExist:
            return Response({"error": "Timetable not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TimetableSerializer(speciality, data=request.data, partial=True)
        speciality.delete()
        return Response({"message": "Timetable deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
