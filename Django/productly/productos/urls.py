from django.urls import path
from . import views  # debe tener el punto para dirigir a ese archivo

app_name = "productos"

urlpatterns = [
    path("", views.index, name="index"),
    path("formulario", views.formulario, name="formulario"),
    path("<int:producto_id>", views.detalle, name="detalle"),
]
