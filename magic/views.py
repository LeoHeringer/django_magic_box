from rest_framework.decorators import api_view, permission_classes, renderer_classes, parser_classes
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Box, Subscription, Shipment, Review, Promotion
from .serializers import ProductSerializer, BoxSerializer, SubscriptionSerializer, ShipmentSerializer, ReviewSerializer, PromotionSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([XMLRenderer, JSONRenderer])
@parser_classes([XMLParser, JSONParser])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([XMLRenderer, JSONRenderer])
@parser_classes([XMLParser, JSONParser])
def create_box(request):
    serializer = BoxSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([XMLRenderer, JSONRenderer])
@parser_classes([XMLParser, JSONParser])
def create_subscription(request):
    serializer = SubscriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([XMLRenderer, JSONRenderer])
@parser_classes([XMLParser, JSONParser])
def create_shipment(request):
    serializer = ShipmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([XMLRenderer, JSONRenderer])
@parser_classes([XMLParser, JSONParser])
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([XMLRenderer, JSONRenderer])
@parser_classes([XMLParser, JSONParser])
def create_promotion(request):
    serializer = PromotionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
