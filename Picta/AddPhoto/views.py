from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Imagen
from .serializers import ImageSerializer
# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
    
    def get_queryset(self):
        creator = self.request.user
        return Imagen.objects.filter(visibility='public') | Imagen.objects.filter(creator=creator)