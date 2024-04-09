from django.shortcuts import render
from .models import Ads

# Create your views here.
def home(request, city=""):
    if city:
        items = Ads.all_for_loc(city)
    else:
        items = Ads.objects.all()
    return render(request, "home.html", {"ads": items, "loc": city})