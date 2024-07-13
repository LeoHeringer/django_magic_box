---

# Magic Box API

## Description

Magic Box API is a Django REST application that manages products, subscription boxes, subscriptions, shipments, reviews, and promotions. The API supports both JSON and XML data formats.

## Models

### Product

```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image_url = models.URLField(max_length=200, blank=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
```

### Box

```python
class Box(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField(Product, related_name='boxes')
    subscription_type = models.CharField(max_length=50, choices=[
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
```

### Subscription

```python
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('active', 'Active'),
        ('canceled', 'Canceled'),
        ('expired', 'Expired'),
    ])
    shipping_address = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.box.title}'
```

### Shipment

```python
class Shipment(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    shipment_date = models.DateTimeField()
    tracking_number = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ('shipped', 'Shipped'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('returned', 'Returned'),
    ])

    def __str__(self):
        return f'Shipment {self.tracking_number} for {self.subscription}'
```

### Review

```python
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'Review {self.user.username} for {self.box.title}'
```

### Promotion

```python
class Promotion(models.Model):
    code = models.CharField(max_length=50)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.code
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/magic-box-api.git
    ```
2. Navigate to the project directory:
    ```bash
    cd magic-box-api
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    ```bash
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Add the renderers and parsers for XML in your `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework_xml.parsers.XMLParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
```

## Usage

### Endpoints

The API provides endpoints to create, list, update, and delete the following resources:

- **Product**
- **Box**
- **Subscription**
- **Shipment**
- **Review**
- **Promotion**

### View Example

The views are configured to accept and render XML and JSON:

```python
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
```
