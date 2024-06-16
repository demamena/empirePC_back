
from parler_rest.serializers import TranslatableModelSerializer

from main.mixins.mixins import TranslatedSerializerMixin, PictureMixin
from main.models import Review


class ReviewSerializer(TranslatedSerializerMixin, PictureMixin, TranslatableModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'name', 'text', 'rating')
        read_only_fields = fields
