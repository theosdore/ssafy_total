from django.shortcuts import render, get_object_or_404, redirect
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


def detail(request, id):
  bakery = Bakery.objects.filter(id=id).first()
  
  bakery = get_object_or_404(Bakery, id = id)

  context = {
    'bakery' : bakery
  }

  return render(request, "bakeries/detail.html", context)

def create(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("name")
        address = request.POST.get("address")
        rating = request.POST.get("rating")
        opening_time = request.POST.get("opening_time")
        closing_time = request.POST.get("closing_time")
        Bakery.objects.create(
          name=name,
          address=address,
          rating=rating,
          opening_time=opening_time,
          closing_time=closing_time,
        )
        return redirect("bakeries:index")
    else:
        return render(request, "bakeries/create.html")
    

