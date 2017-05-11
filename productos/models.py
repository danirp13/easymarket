from django.db import models

# Create your models here.
class Usuario(models.Model):
	usuario = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=100)
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	cedula = models.IntegerField(max_length=50, unique=True)
	celular = models.IntegerField(max_length=50)
	def __str__(self):
		return (self.nombres, self.apellidos)


class Categoria(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	descripcion = models.CharField(max_length=100)
	def __str__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	cantidad = models.IntegerField()
	precio = models.IntegerField()
	fecha_ingreso = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.nombre


class Cliente(models.Model):
	cedula = models.IntegerField(max_length=80, unique=True)
	nombre = models.CharField(max_length=100)	
	apellidos = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, help_text='un correo electronico valido por favor')
	celular = models.IntegerField(max_length=100)
	def __str__(self):
		return (self.nombre,self.apellidos)



class Venta(models.Model):
	cantidad_venta = models.IntegerField()
	valor = models.IntegerField()
	fecha_venta = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return (self.cantidad_venta,self.valor)
