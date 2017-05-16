from django.contrib import admin
from productos.models import CategoriaProductos, Productos, Clientes, Ventas
# Register your models here.

admin.site.register(CategoriaProductos)
admin.site.register(Productos)
admin.site.register(Clientes)
admin.site.register(Ventas)

