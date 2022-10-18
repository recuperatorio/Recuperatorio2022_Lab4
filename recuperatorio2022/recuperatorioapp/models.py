from django.db import models

# Create your models here.

class Cliente  (models.Model):
     idcliente = models.CharField(max_lenght=20)
     apellido = models.CharField(max_lenght=20)
     nombre = models.CharField(max_lenght=20)
     
     
class Factura (models.Model):

      fecha = models.CharField (max_lenght=20)
      condicion = models.Charfield (max_lenght=20)
      cliente = models.ForeignKey('Cliente',on_delete=models.CASCADE)
class DetalleFactura (models.Model):

       producto = models.Charfield(max_lenght=20)
       cantidad = models.Charfield(max_lenght=20)
       
class Producto (models.Model)

        idproducto = models.CharField(max_lenght=20)
        detalle = models.CharField (max_lenght=20)
        precio = models.CharField (max_lenght=20)
