from django.urls import path
from .views import MyOrderView, CreateOrderProductView, eliminar_orden

urlpatterns = [
    path('mi-orden/', MyOrderView.as_view(), name='mi_orden'),
    path('agregar-producto/', CreateOrderProductView.as_view(), name='agregar_producto'),
    path('eliminar-orden/<int:order_id>/', eliminar_orden, name='eliminar_orden'),  # esta línea es clave
]

