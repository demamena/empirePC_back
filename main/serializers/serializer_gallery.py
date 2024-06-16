from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer

from main.mixins.mixins import TranslatedSerializerMixin, PictureMixin
from main.models import GalleryItem, Gallery


class GalleryItemSerializer(TranslatedSerializerMixin, PictureMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=GalleryItem)

    class Meta:
        model = GalleryItem
        fields = ('id', 'translations', 'file',)
        read_only_fields = fields


class GallerySerializer(TranslatedSerializerMixin, PictureMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Gallery)
    items = GalleryItemSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ('id', 'translations', 'items')
        read_only_fields = fields
