from django.db import models

from shared.models import BaseModel


class Taxi(BaseModel):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    region = models.ForeignKey('region.Region', on_delete=models.CASCADE)
    discrict = models.ForeignKey('region.District', on_delete=models.CASCADE)
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
