from __future__ import unicode_literals

from django.db import models
from . import views
import datetime
from django.utils import timezone


# Create your models here.
class Users(models.Model):
    Fname = models.CharField(max_length=255)
    Lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Secrets(models.Model):
    author  = models.ForeignKey(Users, related_name="Secrets")
    secrets = models.CharField(max_length=255)
    likes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
