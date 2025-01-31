from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Imagen
from .serializers import ImageSerializer


# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Image.objects.filter(creator=self.request.user) | Image.objects.filter(is_public=True)
        else:
            return Image.objects.filter(is_public=True)

    def get_serializer_class(self):
            return ImageSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)