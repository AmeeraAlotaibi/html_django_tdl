from django.shortcuts import render
from .models import IceCream

# Create your views here.
def get_ice_cream(request, ice_cream_id):
    ice_cream = IceCream.objects.get(id=ice_cream_id)
    context = { 
        "ice_cream": {
            "name": ice_cream.name,
            "shop": ice_cream.shop,
            "flavors": ice_cream.flavors,
            "stock": ice_cream.stock
        }
    }
    return render(request, "ice_cream.html", context)

def get_all_ice_creams(request):
    ice_creams = IceCream.objects.all()
    context = {
        "ice_creams": ice_creams,
    }
    return render(request, "ice_cream_list.html", context)