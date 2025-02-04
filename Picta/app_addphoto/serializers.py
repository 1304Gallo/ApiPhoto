from rest_framework import serializers
from app_addphoto.models import Imagen

class ImagenSerializer(serializers.ModelSerializer):
    creator_name = serializers.CharField(source='creator.username', read_only=True)

    class Meta:
        model = Imagen
        #fields = ['id', 'creator_name', 'title', 'image_file', 'is_public']
        fields = "__all__"
        read_only_fields = ['id', 'creator']