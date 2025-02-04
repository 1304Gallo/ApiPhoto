from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Imagen
from .serializers import ImagenSerializer


# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ImagenSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Imagen.objects.filter(creator=self.request.user) | Imagen.objects.filter(is_public=True)
        else:
            return Imagen.objects.filter(is_public=True)

   # def get_serializer_class(self):
     #       return ImagenSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)