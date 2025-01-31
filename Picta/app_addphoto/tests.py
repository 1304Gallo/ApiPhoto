from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Imagen

# Create your tests here.
class ImageViewSetTests(APITestCase):

    def setUp(self):
        # Crear un usuario para las pruebas
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')  # Iniciar sesión

        # URL para las pruebas
        self.url = reverse('imagen-list')  # Asegúrate de que el nombre coincida con tu configuración de URL

    def test_create_imagen(self):
        # Prueba la creación de una imagen
        with open('D:/rodri.jpg', 'rb') as image_file:  # Asegúrate de que la ruta sea correcta
            response = self.client.post(self.url, {
                'title': 'Test Image',  # Título de la imagen
                'image_file': image_file,  # Cambia 'imagen' a 'image_file'
                'is_public': True  # O False, según lo que desees probar
            }, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Imagen.objects.count(), 1)
        self.assertEqual(Imagen.objects.get().creator, self.user)
        self.assertEqual(Imagen.objects.get().title, 'Test Image')