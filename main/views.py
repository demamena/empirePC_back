from django.db import transaction

from rest_framework.views import APIView, Response
from rest_framework.authtoken.models import Token

from main.services.service_gallery import get_gallery
from main.services.service_additional import get_price, get_additional_info
from main.services.service_customer import get_customer_info, create_customer, edit_customer
from main.services.service_orders import get_orders, change_order, create_order, get_peripheries
from main.services.service_review import get_reviews, create_review, change_review, delete_review, get_reviews_rating


class CustomerAPIView(APIView):
    def get(self, request):
        try:
            info = get_customer_info(request.user)
        except Exception as e:
            return Response(str(e), status=400)

        return Response(info)

    @transaction.atomic
    def post(self, request):
        try:
            customer = create_customer(
                request.data.get('email'), request.data.get('first_name'),
                request.data.get('last_name'), request.data.get('phone'),
                request.data.get('middle_name', ''), request.data.get('username', ''),
                request.data.get('birthday'), request.data.get('password'))
        except:
            return Response("Can't create customer", status=400)

        token, _ = Token.objects.get_or_create(user=customer)
        return Response({'token': token.key}, status=201)

    @transaction.atomic
    def patch(self, request):
        try:
            edit_customer(
                request.user.id, request.data.get('email'),
                request.data.get('first_name'), request.data.get('last_name'),
                request.data.get('phone'), request.data.get('middle_name'),
                request.data.get('username'), request.data.get('birthday'),
                request.data.get('password'))
        except:
            return Response("Can't edit customer", status=400)

        return Response("Customer updated", status=200)


class OrderAPIView(APIView):
    def get(self, request):
        try:
            orders = get_orders(request.user)
        except:
            return Response("Can't get orders", status=400)

        return Response(orders)

    @transaction.atomic
    def post(self, request):
        try:
            create_order(
                request.user, phone=request.data.get('phone'),
                price=request.data.get('price'), preferences=request.data.get('preferences'),
                wishes=request.data.get('wishes'), call_time=request.data.get('call_time'),
                delivery_type=request.data.get('delivery_type'), type=request.data.get('type'),
                pc_type=request.data.get('pc_type'), graphic_card=request.data.get('graphic_card'),
                processor=request.data.get('processor'), os=request.data.get('os'),
                cooling=request.data.get('cooling'), peripheries=request.data.get('peripheries'),
                setup=request.data.get('setup'), tasks=request.data.get('tasks'),
                presets=request.data.get('presets'))
        except:
            return Response("Can't create order", status=400)

        return Response("Order created", status=201)

    @transaction.atomic
    def patch(self, request, order_id: int):
        try:
            change_order(
                order_id, request.user, phone=request.data.get('phone'),
                price=request.data.get('price'), preferences=request.data.get('preferences'),
                wishes=request.data.get('wishes'), call_time=request.data.get('call_time'),
                delivery_type=request.data.get('delivery_type'), type=request.data.get('type'),
                status=request.data.get('status'), pc_type=request.data.get('pc_type'),
                graphic_card=request.data.get('graphic_card'), processor=request.data.get('processor'),
                cooling=request.data.get('cooling'), os=request.data.get('os'),
                setup=request.data.get('setup'), tasks=request.data.get('tasks'),
                presets=request.data.get('presets'), peripheries=request.data.get('peripheries'))
        except:
            return Response("Can't change order", status=400)

        return Response("Order updated", status=200)


class PeripheryAPIView(APIView):
    def get(self, request):
        try:
            peripheries = get_peripheries()
        except:
            return Response("Can't get peripheries", status=400)

        return Response(peripheries)


class PriceAPIView(APIView):
    def get(self, request, name: str):
        try:
            price = get_price(name)
        except:
            return Response("Can't get price", status=400)

        return Response(price)


class AdditionalInfoAPIView(APIView):
    def get(self, request, name: str):
        try:
            info = get_additional_info(name)
        except:
            return Response("Can't get info", status=400)

        return Response(info)


class ReviewAPIView(APIView):
    def get(self, request):
        try:
            reviews = get_reviews(request.GET.get('count'))
        except:
            return Response("Can't get reviews", status=400)

        return Response(reviews)

    def post(self, request, order_id: int):
        try:
            create_review(
                request.user, order_id, name=request.data.get('name'),
                text=request.data.get('text'), rating=request.data.get('rating'))
        except:
            return Response("Can't create review", status=400)

        return Response('Review created', status=201)

    def patch(self, request, review_id: int):
        try:
            change_review(
                request.user, review_id, name=request.data.get('name'),
                text=request.data.get('text'), rating=request.data.get('rating'))
        except:
            return Response("Can't change review", status=400)

        return Response('Review changed', status=200)

    def delete(self, request, review_id: int):
        try:
            delete_review(request.user, review_id)
        except:
            return Response("Can't delete review", status=400)

        return Response("Review deleted", status=200)


class RatingAPIView(APIView):
    def get(self, request):
        try:
            rating = get_reviews_rating()
        except:
            return Response("Can't get rating", status=400)

        return Response(rating)


class GalleryAPIView(APIView):
    def get(self, request):
        try:
            gallery = get_gallery(request.GET.get('count'))
        except:
            return Response("Can't get gallery", status=400)

        return Response(gallery)
