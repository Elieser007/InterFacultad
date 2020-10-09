from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    foto = models.ImageField(upload_to='profile', null=True,blank=True)
    facebook = models.URLField(
        'Facebook', max_length=200, null=True, blank=True)
    twitter = models.URLField('Twitter', max_length=200, null=True, blank=True)
    instagram = models.URLField(
        'Instagram', max_length=200, null=True, blank=True)
    web = models.URLField('Web', max_length=200, null=True, blank=True)