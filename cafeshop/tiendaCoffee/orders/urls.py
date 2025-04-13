from django.urls import path

from .views import MyOrderView, CreateOrderProductView

urlpatterns = [
    path("mi-orden", MyOrderView.as_view(), name="mi_orden"),
    path("agregar-producto", CreateOrderProductView.as_view(), name="agregar_producto"),
]