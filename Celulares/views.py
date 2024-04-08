from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from Celulares.models import Celular
from Celulares.forms import FormCelular

# Create your views here.


class Inicio():
    
    def home(request):
        return render(request, 'home.html')
    
    def registrarse(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Usuario {username} creado con éxito.')
                return redirect('indice')
        else:
            form = UserRegisterForm()
        return render(request, 'registrarUsuario.html', {'form': form})

    def iniciarSesion(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                return redirect('indice')
            else:
                messages.error(request, 'Nombre de usuario o contraseña no válidos')
        return render(request, 'loguearUsuario.html')
    
    def listarProducto(request):
        products = Celular.objects.all()
        return render(request, 'listarProducto.html', {'products': products})

    @login_required
    def cerrarSesion(request):
        logout(request)
        return redirect('indice')
    
    @login_required
    def eliminarProducto(request, id):
        product = Celular.objects.get(id = id)
        product.delete()
        return redirect('listarProducto')
    
    @login_required
    def actualizarProducto(request, id):
        product = Celular.objects.get(id = id)
        form = FormCelular(instance=product)
        if request.method == 'POST':
            form = FormCelular(request.POST, instance=product)
            if form.is_valid():
                form.save()
            return Inicio.index(request)
        data = { 'form' : form}
        return render(request, 'crearProducto.html', data)
    
    @login_required
    def crearProducto(request):
        if request.method == 'POST':
            form = FormCelular(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('indice')
            
        else:
            form = FormCelular()

        return render(request, 'crearProducto.html', {'form': form})
    
    @login_required
    def añadirAlCarrito(request, product_id):
        
        cart_key = f'cart_{request.user.id}'  # Clave única del carrito para cada usuario
        cart = request.session.get(cart_key, {})

        if str(product_id) in cart:
            cart[str(product_id)] += 1
        else:
            cart[str(product_id)] = 1

        request.session[cart_key] = cart

        return redirect('listarProducto')
    
    @login_required
    def verCarrito(request):
        cart_key = f'cart_{request.user.id}'
        cart = request.session.get(cart_key, {})
        products_in_cart = []

        # Calcular el total general
        total_general = 0

        for product_id, quantity in cart.items():
            product = get_object_or_404(Celular, id=product_id)
            total = product.calcular_total(quantity)
            total_general += total  # Sumar al total general
            products_in_cart.append({'product': product, 'quantity': quantity, 'total': total})

        return render(request, 'verCarrito.html', {'cart': products_in_cart, 'total_general': total_general})
    
    @login_required
    def limpiarCarrito(request):
        cart_key = f'cart_{request.user.id}'
        if cart_key in request.session:
            del request.session[cart_key]
        return redirect('verCarrito')
        
    def calcular_total(self, quantity):
        quantity = Celular.precio * quantity
        return quantity

    def save(self, *args, **kwargs):
        # Calcular y actualizar el campo total antes de guardar el objeto
        self.total = self.calcular_total(Celular.quantity)
        super().save(*args, **kwargs)
    
    def comprarProducto(request):
        cart_key = f'cart_{request.user.id}'
        cart = request.session.get(cart_key, {})
        products_in_cart = []

        # Calcular el total general
        total_general = 0

        for product_id, quantity in cart.items():
            product = get_object_or_404(Celular, id=product_id)
            total = product.calcular_total(quantity)
            total_general += total  # Sumar al total general
            products_in_cart.append({'product': product, 'quantity': quantity, 'total': total})

        return render(request, 'boleta.html', {'cart': products_in_cart, 'total_general': total_general})