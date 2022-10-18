from django.contrib import admin
from . import models
# Register your models here.

 admin.site.register(models.Cliente)
 admin.site.register(models.Factura)
 admin.site.register(models.DetalleFactura)
 admin.site.register(models.Producto)
