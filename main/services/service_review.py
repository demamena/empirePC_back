from main.models import Price, AdditionalInfo, Review, Customer, Order
from main.serializers.serializer_additional import AdditionalInfoSerializer
from main.serializers.serializer_review import ReviewSerializer


def get_reviews(count: int) -> list[dict]:
    count = int(count) if count else 999
    return ReviewSerializer(Review.objects.all()[:count], many=True).data


def create_review(customer: Customer, order_id: int, **kwargs) -> None:
    order = Order.objects.get(id=order_id, customer=customer)
    Review.objects.create(
        order=order, order_id=order_id,
        name=kwargs.get('name'), text=kwargs.get('text'),
        rating=kwargs.get('rating'))


def change_review(customer: Customer, review_id: int, **kwargs) -> None:
    review = Review.objects.get(id=review_id, order__customer=customer)

    if kwargs.get('name'):
        review.name = kwargs.get('name')

    if kwargs.get('text'):
        review.text = kwargs.get('text')

    if kwargs.get('rating'):
        review.rating = kwargs.get('rating')

    review.save()


def delete_review(customer: Customer, review_id: int) -> None:
    Review.objects.get(id=review_id, order__customer=customer).delete()
