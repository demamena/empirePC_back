from rest_framework import serializers

from main.mixins.mixins import PictureMixin
from main.models import Customer


class CustomerSerializer(PictureMixin, serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'email',
                  'phone', 'bonus', 'username', 'birthday')
        read_only_fields = fields
