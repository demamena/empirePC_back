from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer

from main.mixins.mixins import TranslatedSerializerMixin, PictureMixin
from main.models import AdditionalInfo


class AdditionalInfoSerializer(TranslatedSerializerMixin, PictureMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=AdditionalInfo)

    class Meta:
        model = AdditionalInfo
        fields = ('id', 'translations', 'name', 'available')
        read_only_fields = fields
