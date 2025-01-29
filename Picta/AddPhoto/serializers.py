from rest_framework import serializers
from .models import Imagen

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ['id', 'creator', 'title', 'image_file', 'is_public']
        read_only_fields = ['creator']