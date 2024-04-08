from django.shortcuts import render
from .models import Ads

# Create your views here.
def home(request):
    items = Ads.objects.all()
    return render(request, "home.html", {"ads": items})