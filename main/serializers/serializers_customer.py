from rest_framework import serializers

from main.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'email',
                  'phone', 'bonus', 'username', 'birthday')
        read_only_fields = fields
