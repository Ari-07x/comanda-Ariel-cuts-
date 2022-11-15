from rest_framework.routers import DefaultRouter
from pyAPI.api import BusinessApiViewSet, TableApiViewSet, OrderApiViewSet, ReviewApiViewSet, ProductApiViewSet, SupplierApiViewSet,PromoApiViewSet,ContactApiViewSet,StaffApiViewSet

router_business = DefaultRouter()
router_table = DefaultRouter()
router_order = DefaultRouter()
router_review = DefaultRouter()
router_product = DefaultRouter()
router_supplier = DefaultRouter()
router_promo = DefaultRouter()
router_contact = DefaultRouter()
router_staff = DefaultRouter()

router_business.register(prefix='', basename='business', viewset=BusinessApiViewSet)
router_table.register(prefix='', basename='table', viewset=TableApiViewSet)
router_order.register(prefix='', basename='order', viewset=OrderApiViewSet)
router_review.register(prefix='', basename='review', viewset=ReviewApiViewSet)
router_product.register(prefix='', basename='product', viewset=ProductApiViewSet)
router_supplier.register(prefix='', basename='supplier', viewset=SupplierApiViewSet)
router_promo.register(prefix='', basename='promo', viewset=PromoApiViewSet)
router_contact.register(prefix='', basename='contact', viewset=ContactApiViewSet)
router_staff.register(prefix='', basename='staff', viewset=StaffApiViewSet)
