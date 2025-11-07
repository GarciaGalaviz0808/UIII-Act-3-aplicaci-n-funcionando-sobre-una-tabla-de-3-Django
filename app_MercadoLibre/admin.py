from django.contrib import admin
from .models import Vendedor, Categoria, Producto

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ("id_vendedor", "nombre", "apellido", "email", "telefono", "ciudad", "fecha_registro")
    search_fields = ("nombre", "apellido", "email", "ciudad")

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id_categoria", "nombre", "tipo", "activa")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id_producto", "nombre", "vendedor", "precio", "stock", "disponible")