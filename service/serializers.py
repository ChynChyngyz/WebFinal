from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Service
    """
    class Meta:
        model = Service
        # fields = ['title', 'price', 'description', 'image', 'speciality']
        fields = '__all__'

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
