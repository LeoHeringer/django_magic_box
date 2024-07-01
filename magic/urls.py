from django.urls import path
from .views import create_product, create_box, create_subscription, create_shipment, create_review, create_promotion

urlpatterns = [
    path('create_product/', create_product, name='create_product'),
    path('create_box/', create_box, name='create_box'),
    path('create_subscription/', create_subscription, name='create_subscription'),
    path('create_shipment/', create_shipment, name='create_shipment'),
    path('create_review/', create_review, name='create_review'),
    path('create_promotion/', create_promotion, name='create_promotion'),
]
