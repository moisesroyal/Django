from django.views import generic
from .forms import ProductForm
from .models import Product
from django.urls import reverse_lazy

class ProductFormView(generic.FormView):
    template_name = 'productos/misproductos.html'
    form_class = ProductForm
    success_url = reverse_lazy('agregar_producto')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProductListView(generic.ListView):
    template_name = 'productos/lista_producto.html'
    context_object_name = 'productos'
    model = Product

    