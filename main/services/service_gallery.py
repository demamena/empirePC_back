from main.models import Gallery
from main.serializers.serializer_gallery import GallerySerializer


def get_gallery(count: int) -> list[dict]:
    count = int(count) if count else 999
    return GallerySerializer(Gallery.objects.all()[:count], many=True).data


