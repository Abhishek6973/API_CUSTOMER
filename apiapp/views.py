from django.shortcuts import render
from rest_framework import viewsets,status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class CustomerViewsets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class PurchaseViewsets(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class shippingViewsets(viewsets.ModelViewSet):
    queryset = shipping_details.objects.all()
    serializer_class = ShipingSerializer

class CustomerWithShipmentView(APIView):
    def get(self, request, city, format=None):
        try:
            # Retrieve customers with shipment details based on the selected city in shipping details
            customers_with_shipment = Customer.objects.filter(
                shipping_details__city=city
            ).distinct()

            # Serialize the data using the updated serializer
            serializer = CustomerSerializer(customers_with_shipment, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
class CustomerWithPurchaseView(APIView):
    def get(self, request, format=None):
        try:
            # Retrieve all customers with their associated purchase orders
            customers_with_purchase = Customer.objects.all().prefetch_related('purchase_set')

            # Print the data for debugging
            print(customers_with_purchase)

            # Serialize the data using the updated serializer
            serializer = CustomerWithPurchaseSerializer(customers_with_purchase, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CustomerWithPurchaseAndShipmentView(APIView):
    def get(self, request, format=None):
        try:
            # Retrieve all customers with their associated purchase orders and shipment details
            customers_with_purchase_and_shipment = Customer.objects.all().prefetch_related(
                'purchase_set__shipping_details_set'
            )

            # Serialize the data using the updated serializer
            serializer = CustomerWithPurchaseAndShipmentSerializer(customers_with_purchase_and_shipment, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


