from django.shortcuts import render
from .models import Bakery
# Create your views here.
def index(request):
  bakeries = Bakery.objects.all()
  for bakery in bakeries:
    print(f"{bakery.name} / {bakery.rating}")
  context = {
    "bakeries": bakeries
  }
  return render(request, "bakeries/index.html", context)