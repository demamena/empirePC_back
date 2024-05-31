from django.contrib import admin
from django.urls import path

from main.views import CustomerAPIView, PeripheryAPIView, PriceAPIView, AdditionalInfoAPIView, ReviewAPIView, \
    GalleryAPIView

urlpatterns = [
    path('customer/', CustomerAPIView.as_view(), name='customer'),
    path('order/', CustomerAPIView.as_view(), name='orders'),
    path('order/<int:order_id>', CustomerAPIView.as_view(), name='order'),
    path('periphery/', PeripheryAPIView.as_view(), name='periphery'),
    path('prices/<str:name>', PriceAPIView.as_view(), name='price'),
    path('additional-info/<str:name>', AdditionalInfoAPIView.as_view(), name='additional-info'),
    path('reviews/', ReviewAPIView.as_view(), name='review'),
    path('reviews/<int:order_id>', ReviewAPIView.as_view(), name='review add'),
    path('reviews/<int:review_id>', ReviewAPIView.as_view(), name='review patch/delete'),
    path('gallery/', GalleryAPIView.as_view(), name='gallery'),
]
