from modeltranslation.translator import register, TranslationOptions

from .models import Facilities


@register(Facilities)
class FacilitiesTranslationOptions(TranslationOptions):
    fields = ('name',)
