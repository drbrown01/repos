from __future__ import unicode_literals

from django.db import models
from . import views

# Create your models here.
class Users(models.Model):
    Fname = models.CharField(max_length=255)
    Lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    

class Secrets(models.Model):
    secrets = models.CharField(max_length=255)
    likes = models.IntegerField()
