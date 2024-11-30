from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        # указывается все поля модели, которые должны быть в JSON
        fields = ['id', 'is_active', 'nickname', 'email', 'first_name', 'last_name', 'password', 'role']

    @staticmethod
    def create(validated_data, **kwargs):
        # Создаём пользователя, передавая дополнительные данные
        validated_data.setdefault('role', 'User')
        return get_user_model().objects.create_user(**validated_data)


class DoctorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['nickname', 'email', 'first_name', 'last_name', 'password', 'role']

    @staticmethod
    def create(validated_data, **kwargs):
        validated_data.setdefault('role', 'Doctor')
        return get_user_model().objects.create_user(**validated_data)
