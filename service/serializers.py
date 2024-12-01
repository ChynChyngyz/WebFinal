from rest_framework import serializers
from .models import Service
from authUser.models import CustomUser
from drf_spectacular.utils import extend_schema_field


class DoctorForServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'nickname', 'speciality', 'education', 'description']


class ServiceSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Service
    """
    doctor = DoctorForServicesSerializer(many=True, read_only=True)
    doctor_id = DoctorForServicesSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'title', 'doctor', 'doctor_id', 'price', 'description', 'image', 'image_url', 'speciality']

    @extend_schema_field(serializers.URLField)
    def get_image_url(self, obj):
        """
        Возвращаем полный URL изображения для сериализатора
        """
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

    image_url = serializers.SerializerMethodField('get_image_url')
