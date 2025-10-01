from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            #자동 로그인
            auth_login(request,user)
            return redirect("bakeries:index")
    else:
        form = SignupForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect("bakeries:index")
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nextUrl = request.GET.get('next')
            user = form.get_user()
            auth_login(request, user)
            if nextUrl:
                return redirect(nextUrl)
            return redirect("bakeries:index")
    else:
        form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('bakeries:index')
