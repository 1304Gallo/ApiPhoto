# Generated by Django 5.1.5 on 2025-01-28 17:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AddPhoto', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Imagen',
        ),
    ]
