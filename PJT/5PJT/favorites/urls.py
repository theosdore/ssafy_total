from django.urls import path
from . import views

app_name = "favorites"
urlpatterns = [
    path("", views.index, name = 'index'),
    path("addFav/", views.addFavCompany, name='addFav'),
    path("<int:fav_id>/delete/", views.deleteFav, name= "deleteFav")
]
