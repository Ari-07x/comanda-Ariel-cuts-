from unicodedata import name
from django.db import models

# Este es mi modelo de los Negocios
class Business(models.Model):
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    website = models.CharField(max_length=80, null=True, blank=True)
    facebook = models.CharField(max_length=80, null=True, blank=True)
    instagram = models.CharField(max_length=80, null=True, blank=True)
    twitter = models.CharField(max_length=80, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Este es mi modelo de las Mesas
class Table(models.Model):
    table_number = models.IntegerField()
    chairs = models.IntegerField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.table_number

# Este es el modelo de Proveedores (Sole)
class Supplier (models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=80, null=True, blank=True)
    cuit = models.CharField(max_length=40)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BinaryField(max_length=1)

    def __str__(self):
        return self.name


# Este es el modelo de los Productos (Sole)
class Product(models.Model):
     name = models.CharField(max_length=40)
     description = models.CharField(max_length=255)
     sealing_price = models.FloatField()
     cost_price = models.FloatField()
     suppliers = models.ForeignKey(Supplier, null=True, blank=True, on_delete=models.CASCADE)
     stock = models.IntegerField()
     status = models.BinaryField(max_length=1)
     created_at = models.DateTimeField(auto_now_add=True)
     
     
     def __str__(self):
        return self.name

# Este es mi modelo de las Ordenes
class Order(models.Model):
    order_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
   # products = models.ManyToManyRel(Product)
    
    

    def __str__(self):
        return self.order_number    

# Este es mi modelo de las Reseñas
class Review(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    review_text = models.TextField()
    date_review = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.email




    

# Este es el modelo de los Promociones (Sole)
class Promo(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40, null=True, blank=True)
    description = models.CharField(max_length=255)
    sealing_price = models.FloatField()
    status = models.BinaryField(max_length=1)
    
    def __str__(self):
        return self.name
    
#Este es el modelo de Contacto (Joana)
class Contact(models.Model):

    date_contact = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    contact_text = models.TextField()
    phone = models.CharField(max_length=80, null=True, blank=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.email

#Este es el modelo de Personal (Joana)
class Staff(models.Model):

    shift = models.CharField(max_length=20)
    name = models.CharField(max_length=80)
    file = models.CharField(max_length=11)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.shift