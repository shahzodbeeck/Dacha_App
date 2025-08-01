from django.db import models
from shared.on_migrate.facilities import *

from shared.models import BaseModel


class Facilities(BaseModel):
    name = models.CharField(max_length=100, blank=True)
