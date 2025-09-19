from django.contrib import admin
from django.urls import path, include
from . import views
app_name="books"
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:menu>/',views.detail, name='detail')
]
