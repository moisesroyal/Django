from django import forms
from .models import OrderProduct, Product


class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = ["product"]