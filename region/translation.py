from modeltranslation.translator import register, TranslationOptions

from .models import Region, District, PopularPlaces


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(PopularPlaces)
class PopularPlacesTranslationOptions(TranslationOptions):
    fields = ('name',)
