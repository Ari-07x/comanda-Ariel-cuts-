from rest_framework import ModelViewSet
from pyApi.models import *
from .serializers import *


class BusinessViewSet(ModelViewSet):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()

class TableViewSet(ModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all()    

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
class SupplierViewSet(ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

class PromoViewSet(ModelViewSet):
    serializer_class = PromoSerializer
    queryset = Promo.objects.all()

class ContactViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

class StaffViewSet(ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
