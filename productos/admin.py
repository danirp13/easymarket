from django.contrib import admin
from productos.models import Usuario, Categoria, Producto, Cliente, Venta
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Venta)
