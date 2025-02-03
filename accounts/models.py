from django.db import models

from django.contrib.auth.models import AbstractUser

#from .models import CustomUser

# Create your models here.

class CustomUser(AbstractUser):
    # 追加のフィールドを定義（例）
    age = models.IntegerField(null=True, blank=True)