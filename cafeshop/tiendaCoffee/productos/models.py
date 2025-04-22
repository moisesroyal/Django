from django.db import models

class Product(models.Model):
    nombre = models.TextField(max_length=200, verbose_name="Nombre del producto")
    descripcion = models.TextField(max_length=500, verbose_name="Descripción del producto")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio del producto")
    available = models.BooleanField(default=True, verbose_name="¿Está disponible?")
    photo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name="Foto del producto")

    def __str__(self):
        return self.nombre
