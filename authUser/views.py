from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserSerializer, DoctorSerializer
from .models import CustomUser

from drf_spectacular.utils import extend_schema  # OpenApiParameter, OpenApiExample
# from drf_spectacular.types import OpenApiTypes


class RegisterView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=UserSerializer,
        responses={201: {"message": "User created successfully"}},
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Создаём нового пользователя
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        responses={200: UserSerializer()},
    )
    def get(self, request):
        serializer = UserSerializer(data=request.data)
        user = request.user
        return Response({
            "nickname": user.nickname,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "id": user.id
        })


class AllUsersView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        responses={200: UserSerializer(many=True)},
    )
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DoctorView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        responses={200: DoctorSerializer(many=True)},
    )
    def get(self, request):
        doctor = request.doctors
        serializer = DoctorSerializer(doctor, many=True)
        return Response({
            "nickname": doctor.nickname,
            "email": doctor.email,
            "first_name": doctor.first_name,
            "last_name": doctor.last_name,
            "role": doctor.role,
            "id": doctor.id
        })
