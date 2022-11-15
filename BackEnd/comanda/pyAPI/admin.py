from django.contrib import admin
from .models import *

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "phone", "email", "website", "created_at")
    search_fields = ["name", "email", "address"]

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("id", "table_number", "chairs", "business", "created_at")
    search_fields = ["table_number", "chairs", "business"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "table_id", "order_number", "created_at")
    search_fields = ["id", "table_id", "order_number", "created_at"]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "review_text", "date_review", "rate")
    search_fields = ["name", "email", "review_text"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #Lista de campos para administrar
    list_display = ("id", "name", "description", "sealing_price", "cost_price", "suppliers","stock","status","created_at")
    #Lista de campos de busqueda
    search_fields = ["name", "description", "suppliers"]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    #Lista de campos para administrar
    list_display = ("id", "name", "address", "phone", "cuit", "email","status")
    #Lista de campos de busqueda
    search_fields = ["name", "cuit", "email"]

@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    #Lista de campos para administrar
    list_display = ("id", "order_date","name", "description", "sealing_price","status")
    #Lista de campos de busqueda
    search_fields = ["order_date","name", "description"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    #Lista de campos para administrar
    list_display = ("id", "date_contact", "email", "phone", "contact_text", "business")
    #Lista de campos de busqueda
    search_fields = ["email", "contact_text", "business"]


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    #Lista de campos para administrar
    list_display = ("id", "shift", "name","file", "business")
    #Lista de campos de busqueda
    search_fields = ["name","file", "business"]
