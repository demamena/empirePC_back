
from parler_rest.serializers import TranslatableModelSerializer

from main.mixins.mixins import TranslatedSerializerMixin
from main.models import Review


class ReviewSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'name', 'text', 'mark', 'verified')
        read_only_fields = fields
