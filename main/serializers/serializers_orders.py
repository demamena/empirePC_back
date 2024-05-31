from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import serializers

from main.mixins.mixins import TranslatedSerializerMixin
from main.models import Order, WorkTask, ProgramPreset


class WorkTaskSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=WorkTask)

    class Meta:
        model = WorkTask
        fields = ('id', 'name', 'translations')
        read_only_fields = fields


class ProgramPresetSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=ProgramPreset)

    class Meta:
        model = ProgramPreset
        fields = ('id', 'name', 'translations')
        read_only_fields = fields


class PeripherySerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=ProgramPreset)

    class Meta:
        model = ProgramPreset
        fields = ('id', 'name', 'translations')
        read_only_fields = fields


class OrderSerializer(serializers.ModelSerializer):
    tasks = WorkTaskSerializer(many=True, read_only=True)
    presets = ProgramPresetSerializer(many=True, read_only=True)
    peripheries = PeripherySerializer(many=True, read_only=True)
    review_available = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'phone', 'date', 'price', 'preferences',
                  'wishes', 'call_time', 'delivery_type', 'type',
                  'status', 'pc_type', 'graphic_card', 'processor',
                  'cooling', 'os', 'setup', 'tasks', 'presets',
                  'peripheries', 'review_available')
        read_only_fields = fields

    def get_review_available(self, obj):
        return bool(obj.review)
