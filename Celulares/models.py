from django.db import models
from decimal import Decimal

# Create your models here.

OPCIONES_MARCA = (
        ('Samsung', 'Samsung'),
        ('Apple', 'Apple'),
        ('Xiaomi', 'Xiaomi'),
        ('Motorola', 'Motorola'),
    )

class Celular(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    quantity = models.IntegerField(null=True, blank=True, default=0)
    marca = models.CharField(max_length=50, choices=OPCIONES_MARCA, null=True, blank=True)
    foto = models.ImageField(upload_to='webVentas', null=True, blank=True)
    descripcion = models.TextField(verbose_name="Descripción", null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")

    def calcular_total(self, quantity):
        quantity = self.precio * quantity
        return quantity

    def save(self, *args, **kwargs):
        # Calcular y actualizar el campo total antes de guardar el objeto
        self.total = self.calcular_total(self.quantity)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
    
