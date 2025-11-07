from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio_mercadolibre, name="inicio"),
    path("vendedor/agregar/", views.agregar_vendedor, name="agregar_vendedor"),
    path("vendedor/ver/", views.ver_vendedor, name="ver_vendedor"),
    path("vendedor/actualizar/<int:id_vendedor>/", views.actualizar_vendedor, name="actualizar_vendedor"),
    path("vendedor/realizar_actualizacion/<int:id_vendedor>/", views.realizar_actualizacion_vendedor, name="realizar_actualizacion_vendedor"),
    path("vendedor/borrar/<int:id_vendedor>/", views.borrar_vendedor, name="borrar_vendedor"),
]