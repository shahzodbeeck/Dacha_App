from django.db import models


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
