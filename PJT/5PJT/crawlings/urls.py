from django.urls import path
from . import views

app_name = "crawlings"
urlpatterns = [
    path("", views.index, name = 'index'),
    path("crawling/", views.crawling, name = "crawling"),
    path("company/<str:company_code>/", views.print_comment, name="print_comment"),
    path("company/<int:id>/delete", views.delete_comment, name="delete_comment"),
    path("find/", views.find_codename, name="find_codename"),
]
