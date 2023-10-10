from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    nickname = models.CharField(max_length=100, null=False, unique=True)
    image = models.ImageField(upload_to="profile/", null=True)
    message = models.CharField(max_length=200, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')