from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Imagen
from .serializers import ImageSerializer
from django.db.models import Q 
from app_addphoto.services.image_service import ImageService

# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ImageService.get_user_images(self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ImageSerializer

    def perform_create(self, serializer):
        # Utiliza el servicio para crear la imagen
        ImageService.create_image(serializer.validated_data, self.request.user)