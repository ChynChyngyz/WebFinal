from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        # указывается все поля модели, которые должны быть в JSON
        fields = ['id', 'is_active', 'is_staff', 'is_superuser', 'avatar', 'nickname', 'email', 'first_name', 'last_name', 'phone',
                  'date_of_birth', 'password', 'description', 'role']

    @staticmethod
    def create(validated_data, **kwargs):
        password = validated_data.pop('password')

        try:
            validate_password(password)
        except Exception as e:
            raise serializers.ValidationError(str(e))

        validated_data.setdefault('role', 'User')
        user = get_user_model().objects.create_user(password=password, **validated_data)
        return user


class DoctorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'is_staff', 'avatar', 'nickname', 'email', 'first_name', 'last_name', 'phone', 'date_of_birth',
                  'password', 'speciality', 'speciality', 'education', 'description', 'experience', 'role']

    speciality = serializers.CharField(required=True)
    experience = serializers.IntegerField(required=True)
    description = serializers.CharField(required=True)
    education = serializers.CharField(required=True)

    @staticmethod
    def create(validated_data, **kwargs):
        password = validated_data.pop('password')

        try:
            validate_password(password)
        except Exception as e:
            raise serializers.ValidationError(str(e))

        validated_data.setdefault('role', 'Doctor')
        user = get_user_model().objects.create_user(password=password, **validated_data)
        return user
