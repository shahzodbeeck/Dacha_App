from django.db import models

# from shared.on_migrate.region import *  #Regionlarni create qiladi
from shared.models import BaseModel


class Region(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class District(BaseModel):
    name = models.CharField(max_length=100, blank=True)
    province = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PopularPlaces(BaseModel):
    name = models.CharField(max_length=100, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
