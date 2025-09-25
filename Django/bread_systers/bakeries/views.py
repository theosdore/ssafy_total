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
    

def delete(request, id):
   bakery = get_object_or_404(Bakery, id=id)
   bakery.delete()
   print(bakery)
   return redirect("bakeries:index")

import random
from django.utils import timezone

#수정
# 1. 수정 페이지 출력 (GET)
# 2. DB에 데이터 수정 (POST)
def update(request, id):
   bakery = get_object_or_404(Bakery,id=id)
   if request.method == "POST":
      # Todo: 데이터 수정
      name = request.POST.get("name")
      address = request.POST.get("address")
      rating = request.POST.get("rating")
      opening_time = request.POST.get("opening_time")
      closing_time = request.POST.get("closing_time")
      bakery.name = name
      bakery.address = address
      bakery.rating = rating
      bakery.opening_time = opening_time
      bakery.closing_time = closing_time
      bakery.save()
      return redirect("bakeries:detail", bakery.id)
   else:
      context = {
         'bakery' : bakery,
      }
      return render(request, "bakeries/update.html", context)

#-----테스트용
def test(request):
   Bakery.objects.create(
          name="테스트데이터",
          address="하늘나라",
          rating=round(random.uniform(0.0, 5.0),1),
          opening_time=timezone.now(),
          closing_time=timezone.now(),
        )
   return redirect('bakeries:index')