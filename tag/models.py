from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Project(models.Model):
    name=models.CharField(max_length=50)

class Repository(models.Model):
    repository=models.CharField(max_length=100)
    development=models.CharField(max_length=20)
    release=models.CharField(max_length=20)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)

class User(AbstractUser):
    ssh_key = models.TextField(max_length=500, blank=True)
