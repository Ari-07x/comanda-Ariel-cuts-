from rest_framework.viewsets import ModelViewSet
from pyAPI.models import *
from .serializers import *

class BusinessApiViewSet(ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class TableApiViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class OrderApiViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ReviewApiViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ProductApiViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PromoApiViewSet(ModelViewSet):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer

class SupplierApiViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ContactApiViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class StaffApiViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
