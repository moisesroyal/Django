from django import forms
from .models import Product

class ProductForm(forms.Form):
    nombre = forms.CharField(max_length=200, label='Nombre del producto')
    descripcion = forms.CharField(max_length=500, label='Descripción')
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')
    available = forms.BooleanField(initial=True, label='Disponible', required=False)
    photo = forms.ImageField(required=False, label='Foto del producto')

    def save(self):
        Product.objects.create(
            nombre=self.cleaned_data['nombre'],
            descripcion=self.cleaned_data['descripcion'],
            precio=self.cleaned_data['precio'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data['photo']
        )
