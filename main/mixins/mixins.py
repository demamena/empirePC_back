from parler.views import LanguageChoiceMixin

from empirePc import settings
from empirePc.settings import SITE


class TranslatedSerializerMixin(LanguageChoiceMixin):

    def to_representation(self, instance):
        inst_rep = super().to_representation(instance)
        lang_code = self.context.get('language')

        result = {}
        for field_name, field in self.get_fields().items():
            if field_name == 'translations':
                translations = inst_rep.pop(field_name)
                if lang_code not in translations and not self.context.get('is_translate'):
                    # use fallback setting in PARLER_LANGUAGES
                    parler_default_settings = settings.PARLER_LANGUAGES['default']
                    if 'fallback' in parler_default_settings:
                        lang_code = parler_default_settings.get('fallback')

                    if 'fallbacks' in parler_default_settings:
                        lang_code = parler_default_settings.get('fallbacks')[0]
                for lang, translation_fields in translations.items():
                    if lang_code not in translations:
                        for trans_field_name, trans_field in translation_fields.items():
                            result.update({trans_field_name: ''})
                    elif lang == lang_code:
                        trans_rep = translation_fields.copy()  # make copy to use pop() from
                        for trans_field_name, trans_field in translation_fields.items():
                            field_value = trans_rep.pop(trans_field_name)
                            result.update({trans_field_name: field_value})
            else:
                result.update({field_name: inst_rep.pop(field_name)})
        return result


class PictureMixin:

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if 'file' in data and data['file']:
            data['file'] = f'{SITE}{data["file"]}'

        return data
