from django.shortcuts import render
from miprimeraApp.models import Car

# Create your views here.

def my_view(request):
    car_list = Car.objects.all()
    context = { 
        "car_list": car_list 
    }
    return render(request, "miprimeraApp/car_list.html", context)