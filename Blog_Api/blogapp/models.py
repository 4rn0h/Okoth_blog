from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_img", blank=True, null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    Linkedin = models.URLField(max_length=255, blank=True, null=True)
    Twitter = models.URLField(max_length=255, blank=True, null=True)
    Github = models.URLField(max_length=255, blank=True, null=True)
    Dev = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username