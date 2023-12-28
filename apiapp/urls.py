from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewsets)
router.register(r'purchase', PurchaseViewsets)
router.register(r'shipping_details',shippingViewsets)


urlpatterns = [
    path('', include(router.urls)),
    path('customers-with-shipment/<str:city>/', CustomerWithShipmentView.as_view(), name='customer-with-shipment'),
    path('customers-with-purchase/', CustomerWithPurchaseView.as_view(), name='customer-with-purchase'),
    path('customers-with-purchase-and-shipment/', CustomerWithPurchaseAndShipmentView.as_view(), name='customer-with-purchase-and-shipment'),

]