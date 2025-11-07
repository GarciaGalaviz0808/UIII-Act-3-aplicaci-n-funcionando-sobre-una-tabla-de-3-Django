from django.shortcuts import render, redirect, get_object_or_404
from .models import Vendedor

# Página de inicio del sistema
def inicio_mercadolibre(request):
    contexto = {}
    return render(request, "inicio.html", contexto)

# Agregar vendedor (form simple POST)
def agregar_vendedor(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "")
        apellido = request.POST.get("apellido", "")
        email = request.POST.get("email", "")
        telefono = request.POST.get("telefono", "")
        direccion = request.POST.get("direccion", "")
        ciudad = request.POST.get("ciudad", "")
        # No validamos (según tu pedido)
        Vendedor.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            direccion=direccion,
            ciudad=ciudad
        )
        return redirect("ver_vendedor")
    return render(request, "vendedor/agregar_vendedor.html")

# Ver vendedores (lista en tabla)
def ver_vendedor(request):
    vendedores = Vendedor.objects.all().order_by("-fecha_registro")
    return render(request, "vendedor/ver_vendedor.html", {"vendedores": vendedores})

# Actualizar — muestra formulario con datos
def actualizar_vendedor(request, id_vendedor):
    vendedor = get_object_or_404(Vendedor, id_vendedor=id_vendedor)
    return render(request, "vendedor/actualizar_vendedor.html", {"vendedor": vendedor})

# Realizar actualización (POST)
def realizar_actualizacion_vendedor(request, id_vendedor):
    vendedor = get_object_or_404(Vendedor, id_vendedor=id_vendedor)
    if request.method == "POST":
        vendedor.nombre = request.POST.get("nombre", vendedor.nombre)
        vendedor.apellido = request.POST.get("apellido", vendedor.apellido)
        vendedor.email = request.POST.get("email", vendedor.email)
        vendedor.telefono = request.POST.get("telefono", vendedor.telefono)
        vendedor.direccion = request.POST.get("direccion", vendedor.direccion)
        vendedor.ciudad = request.POST.get("ciudad", vendedor.ciudad)
        vendedor.save()
        return redirect("ver_vendedor")
    return redirect("actualizar_vendedor", id_vendedor=id_vendedor)

# Borrar — confirmar y eliminar
def borrar_vendedor(request, id_vendedor):
    vendedor = get_object_or_404(Vendedor, id_vendedor=id_vendedor)
    if request.method == "POST":
        vendedor.delete()
        return redirect("ver_vendedor")
    return render(request, "vendedor/borrar_vendedor.html", {"vendedor": vendedor})