from django.contrib.auth.models import AbstractUser
from django.db import models

from shared.models import BaseModel


class Users(AbstractUser, BaseModel):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    auto_working_time = models.TimeField(null=True, blank=True)
