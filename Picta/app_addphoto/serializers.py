from rest_framework import serializers
from app_addphoto.models import Imagen

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ['id', 'creator', 'title', 'image_file', 'is_public']
        read_only_fields = ['id', 'creator']