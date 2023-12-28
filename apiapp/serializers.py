from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'mobile', 'city')
        
class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchase
        fields = ('id', 'product_name', 'quantity', 'price', 'mrp', 'customer')
        
class ShipingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = shipping_details
        fields = "__all__"
        
class PurchaseWithDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('id', 'product_name', 'quantity', 'price', 'mrp')

class CustomerWithPurchaseSerializer(serializers.ModelSerializer):
    purchase_orders = PurchaseWithDetailsSerializer(many=True, read_only=True, source='purchase_set')
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'mobile', 'city', 'purchase_orders')

class ShippingWithDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = shipping_details
        fields = "__all__"

class CustomerWithPurchaseAndShipmentSerializer(serializers.ModelSerializer):
    purchase_orders = PurchaseWithDetailsSerializer(many=True, read_only=True, source='purchase_set')
    shipping_details_order =ShippingWithDetailSerializer(many=True, read_only=True, source='shipping_details_set')
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'mobile', 'city', 'purchase_orders', 'shipping_details_order')
