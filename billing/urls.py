from billing.views import InvoiceViewset, InvoiceItemViewset, PaymentMethodViewset, PaymentViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'invoice', InvoiceViewset, basename='invoice')
router.register(r'invoiceitem', InvoiceItemViewset, basename='invoiceitem')
router.register(r'paymentmethod', PaymentMethodViewset, basename='paymentmethod')
router.register(r'payment', PaymentViewset, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]