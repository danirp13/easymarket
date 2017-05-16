from django.db import models

# Create your models here.
class CategoriaProductos(models.Model):
    id_categoria = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)


class Productos(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    cantidad = models.BigIntegerField(blank=True, null=True)
    precio = models.BigIntegerField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    id_categoria = models.ForeignKey(CategoriaProductos, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)


 class Clientes(models.Model):
    id_cliente = models.BigIntegerField(primary_key=True)
    cedula = models.BigIntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    apellidos = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    celular = models.BigIntegerField(blank=True, null=True)
    

class Ventas(models.Model):
    id_venta = models.BigIntegerField(primary_key=True)
    cantidad_venta = models.BigIntegerField(blank=True, null=True)
    valor = models.BigIntegerField(blank=True, null=True)
    fecha_venta = models.DateField(blank=True, null=True)
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)       
    productos= models.ManyToManyField(Productos)

