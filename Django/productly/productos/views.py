from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm
from .models import Producto


# Create your views here.


def index(request):
    productos = Producto.objects.all()
    # productos = Producto.objects.filter(puntaje=3)
    # productos = Producto.objects.get(pk=1) #primary key
    # print(productos)
    # return HttpResponse(productos[0].nombre)
    # return HttpResponse("Hola Mundo!")  # en quick fix elegir add "from django"
    # producto_id = 1  # Asigna el ID del producto que deseas consultar

    return render(request, "index.html", context={"productos": productos})


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    return render(request, "detalle.html", context={"producto": producto})


def formulario(request):
    form = ProductoForm()
