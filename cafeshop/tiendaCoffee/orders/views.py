from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .models import Order
from .forms import OrderProductForm

class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/mi_orden.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        # Obtener la orden activa para el usuario, si no existe, crear una nueva
        order = Order.objects.filter(is_active=True, user=self.request.user).first()
        if order is None:
            # Si no existe una orden activa, crear una nueva
            order = Order.objects.create(user=self.request.user, is_active=True)
        return order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()

        # Calcular el total de la orden
        total_price = sum(product_order.product.precio * product_order.quantity for product_order in order.orderproduct_set.all())
        context['total_price'] = total_price
        
        return context


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = "orders/crear_orden.html"
    form_class = OrderProductForm
    success_url = reverse_lazy("mi_orden")

    def form_valid(self, form):
        orden, created = Order.objects.get_or_create(
            is_active=True,
            user=self.request.user,
        )
        if created:
            print("Nueva orden:", orden)
        else:
            print("Ya existe esta orden:", orden)
        
        form.instance.orden = orden
        form.instance.quantity = 1  # O el valor que determines
        form.save()
        return super().form_valid(form)


# Vista para eliminar una orden
from django.contrib.auth.decorators import login_required

@login_required
def eliminar_orden(request, order_id):
    # Obtener la orden activa del usuario
    orden = get_object_or_404(Order, id=order_id, user=request.user)

    # Eliminar la orden
    orden.delete()

    # Redirigir a la vista donde se crea una nueva orden si no hay una activa
    return redirect("mi_orden")  # Redirige a la vista de la orden