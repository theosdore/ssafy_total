from django.urls import path
from . import views

app_name="bakeries"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("<int:id>/delete/", views.delete, name="delete"),
    path("<int:id>/update/", views.update, name="update"),

    # ----- 테스트용
    path("test/", views.test, name="test"),
]
