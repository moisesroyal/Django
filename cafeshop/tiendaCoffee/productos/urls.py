from django.urls import path
from .views import ProductFormView, ProductListView
#     success_url = '/productos/agregar/'
urlpatterns = [
    path('', ProductListView.as_view(), name='lista_productos'),
    path('agregar/', ProductFormView.as_view(), name='agregar_producto'),
]
