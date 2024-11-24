from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  # , IsAdminUser

from .models import Speciality
from .serializers import SpecialitySerializer
# from .forms import SpecialityForm

from django.views.decorators.csrf import csrf_exempt


class SpecialityListView(APIView):
    """
    Класс для вывода списка специализаций.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Метод для получения списка специализаций.
        """
        specialities = Speciality.objects.all()  # Получаем все специализации
        serializer = SpecialitySerializer(specialities, many=True)  # Сериализуем данные
        return Response(serializer.data, status=status.HTTP_200_OK)


# Класс для детального просмотра специализации
# class SpecialityDetailView(APIView):
#     """
#     Класс для вывода детали специализации.
#     """
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         user, doctor = request.user, request.doctor
#         return Response({
#
#         })


# Класс для создания специализации
class SpecialityCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request):
        """
        Метод для создания новой специализации.
        """
        if request.user.role != 'Admin':
            return Response({"error": "Access denied. Only admin can perform this action"},
                            status=status.HTTP_403_FORBIDDEN)

        data = request.data
        serializer = SpecialitySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecialityUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def put(self, request, pk):
        """
        Метод для обновления специализации.
        """
        if request.user.role != 'Admin':
            return Response({"error": "Access denied. Only admin can perform this action"},
                            status=status.HTTP_403_FORBIDDEN)

        try:
            speciality = Speciality.objects.get(pk=pk)  # Нахождение специализации
        except Speciality.DoesNotExist:
            return Response({"error": "Speciality not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SpecialitySerializer(speciality, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecialityDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def delete(self, request, pk):
        """
        Метод для удаления специализации.
        """
        if request.user.role != 'Admin':
            return Response({"error": "Access denied. Only admin can perform this action"},
                            status=status.HTTP_403_FORBIDDEN)

        try:
            speciality = Speciality.objects.get(pk=pk)
        except Speciality.DoesNotExist:
            return Response({"error": "Speciality not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SpecialitySerializer(speciality, data=request.data, partial=True)
        speciality.delete()
        return Response({"message": "Speciality deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class SpecialityListAPIView(APIView):
    """
    API для получения списка специализаций в формате JSON.
    """
    permission_classes = [IsAuthenticated]  # Ограничение доступа для аутентифицированных пользователей

    def get(self, request):
        """
        Метод для получения списка специализаций.
        """
        specialities = Speciality.objects.all()  # Получаем все специализации
        serializer = SpecialitySerializer(specialities, many=True)  # Сериализуем данные
        return Response(serializer.data, status=status.HTTP_200_OK)
