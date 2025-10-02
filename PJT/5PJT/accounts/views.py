from django.shortcuts import render, redirect
from .forms import CustromCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login

# Create your views here.
def signup(request):
  if request.method == "POST":
    form = CustromCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login (request, user)
      return redirect ("crawlings:index")
  else:
    form = CustromCreationForm()
  context = {
    'form': form,
  }
  return render (request, "accounts/singup.html", context)

def login(request):
  # if request.user.is_authenticated:
  #   return redirect("crawlings:index")
  if request.method == "POST":
    form = AuthenticationForm(request.POST, data=request.POST)
    if form.is_valid():
      user =  form.get_user()
      auth_login(request, user)
      return redirect ("crawlings:index")
  else:
    form = AuthenticationForm()
  context = {
    'form': form,
  }
  return render (request, "accounts/login.html", context)
  
def logout(request):
  auth_logout (request)
  return redirect ("crawlings:index")