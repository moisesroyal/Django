from django.shortcuts import render
from miprimeraApp.models import Car
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

def my_view(request):
    car_list = Car.objects.all()
    context = { 
        "car_list": car_list 
    }
    return render(request, "miprimeraApp/car_list.html", context)

class CarListView(TemplateView):
    template_name = "miprimeraApp/car_list.html"

    def get_context_data(self):
        car_list = [
        {"title": "Toyota"},
        {"title": "Hundai"},
        {"title": "Chevrolet"},
        {"title": "Honda"},
        {"title": "BMW"},
        {"title": "Mercedes Benz"},
        {"title": "Ford"},
        {"title": "Nissan"},
        {"title": "Kia"},
        {"title": "Volkswagen"},
        {"title": "Mazda"},
        {"title": "Subaru"},
        {"title": "Audi"},
        {"title": "Lexus"},
        {"title": "Porsche"},
        {"title": "Jaguar"}
       

        ]

        return {
            "car_list": car_list
        }
        


def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)

    # Your view logic here
    return HttpResponse("")