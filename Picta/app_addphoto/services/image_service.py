from django.db.models import Q
from app_addphoto.models import Imagen

class ImageService:
    @staticmethod
    def get_user_images(user):
        return Imagen.objects.filter(
            Q(visibility='public') | 
            Q(creator=user)
        )

    @staticmethod
    def create_image(data, user):
        return Imagen.objects.create(**data, creator=user)