from django.shortcuts import render

# Create your views here.
def index(request): 
    
    menus = ['순대국밥', '김볶밥', '10층']
    
    context = {
        'menus' : menus,
    }
    return render(request,"books/index.html", context)

def detail(request, menu):
    context = {
        'menu' : menu,
    }
    return render(request,"books/detail.html", context)

