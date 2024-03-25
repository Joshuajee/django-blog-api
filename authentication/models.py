from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_img = models.FileField(upload_to="profiles", blank=True)
    search_fields = ('username',)
    
