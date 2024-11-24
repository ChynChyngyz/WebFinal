from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt

from .models import Service
from .serializers import ServiceSerializer

from speciality.models import Speciality
from authUser.models import CustomUser


class ServiceListView(APIView):
    """
    Класс для вывода списка медицинских услуг.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Метод для получения списка объектов услуга.
        """
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServiceDetailView(APIView):
    """
    Класс для просмотра медицинской услуги.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            service = Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service, data=request.data, partial=True)
        service.get()
        return Response({"message": "Service found successfully."}, status=status.HTTP_200_OK)


class SpecialityServiceListView(APIView):
    """
    Класс просмотра списка услуг специализации.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Метод для получения объектов Специализации.
        """
        queryset = super().get_queryset()
        queryset = queryset.filter(speciality=self.kwargs.get('pk'))

        return queryset

    def get_context_data(self, *args, **kwargs):
        """
        Метод для получения списка объектов услуги.
        """
        context_data = super().get_context_data(*args, **kwargs)

        speciality_item = Speciality.objects.get(pk=self.kwargs.get('pk'))
        context_data['speciality_pk'] = speciality_item.pk

        return context_data


class ServiceCreateView(APIView):
    """
    Класс для создания объекта Услуга.
    """
    @csrf_exempt
    def post(self, request):
        """
        Метод для создания новой специализации.
        """
        if request.user.role != 'Admin':
            return Response({"error": "Access denied. Only admin can perform this action"},
                            status=status.HTTP_403_FORBIDDEN)

        data = request.data
        serializer = ServiceSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceUpdateView(APIView):
    """
    Класс для редактирования объекта услуга.
    """
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            service = Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceDeleteView(APIView):
    """
    Класс для удаления объекта услуга.
    """
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            service = Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service, data=request.data, partial=True)
        service.delete()
        return Response({"message": "Speciality deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
