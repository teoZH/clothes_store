from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    image = models.ImageField(upload_to='auth/')
