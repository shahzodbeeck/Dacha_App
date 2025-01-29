from django.db.models.signals import post_migrate
from django.dispatch import receiver

from shared.list.facilities import options


@receiver(post_migrate)
def create_facilities(sender, **kwargs):
    from facilities.models import Facilities
    for province in options:
        Facilities.objects.get_or_create(
            name_uz=province['uz'],
            name_ru=province['ru'],
            name_en=province['en']
        )
