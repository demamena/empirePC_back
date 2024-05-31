from main.models import Price, AdditionalInfo
from main.serializers.serializer_additional import AdditionalInfoSerializer


def get_price(name: str) -> float:
    return Price.objects.get(name=name).price


def get_additional_info(name: str) -> dict:
    return AdditionalInfoSerializer(AdditionalInfo.objects.get(name=name)).data
