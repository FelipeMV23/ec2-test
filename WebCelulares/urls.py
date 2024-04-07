"""
URL configuration for WebCelulares project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from modulo1.views import Practica
from Celulares.views import Inicio
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(' ', Inicio.index, name='indice'),
    path('iniciarSesion/', Inicio.iniciarSesion , name="iniciarSesion"),
    path('registrarse/', Inicio.registrarse, name="registrarUsuario"),
    path('logout/', Inicio.cerrarSesion, name='cerrarSesion'),
    path('listarProducto', Inicio.listarProducto, name="listarProducto"),
    path('eliminarProducto/<int:id>', Inicio.eliminarProducto),
    path('actualizarProducto/<int:id>', Inicio.actualizarProducto),
    path('crearProducto/', Inicio.crearProducto, name='crearProducto'),
    path('añadirAlCarrito/<int:product_id>/', Inicio.añadirAlCarrito, name='añadirAlCarrito'),
    path('verCarrito/', Inicio.verCarrito, name='verCarrito'),
    path('limpiarCarrito/', Inicio.limpiarCarrito, name='limpiarCarrito'),
    path('boleta/', Inicio.comprarProducto, name='boleta')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
