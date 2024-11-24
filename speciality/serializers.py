from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import Speciality


class SpecialitySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Speciality
    """
    class Meta:
        model = Speciality
        # указывается все поля модели, которые должны быть в JSON
        fields = ['id', 'speciality_name', 'description', 'image', 'image_url']

    @extend_schema_field(serializers.URLField)
    def get_image_url(self, obj):
        """
        Возвращаем полный URL изображения для сериализатора
        """
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

    # добавление нового поле для изображения в формате URL
    image_url = serializers.SerializerMethodField('get_image_url')
