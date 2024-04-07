from django.contrib import admin
from Celulares.models import Celular
from django.contrib.auth.models import User
# Register your models here.

@admin.register(Celular)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'quantity', 'marca',  'foto', 'descripcion', 'precio']

