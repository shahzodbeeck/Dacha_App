from django.db.models.signals import post_migrate
from django.dispatch import receiver

from shared.list.regions import provinces_data, districts_data


@receiver(post_migrate)
def create_regions(sender, **kwargs):
    from region.models import Region, District
    for province in provinces_data:
        Region.objects.get_or_create(
            name_uz=province['name_uz'],
            name_ru=province['name_ru'],
            name_en=province['name_en']
        )

    for district in districts_data:
        District.objects.get_or_create(
            name_uz=district['name_uz'],
            name_ru=district['name_ru'],
            name_en=district['name_en'],
            province_id=district['province_id']
        )
