from django.urls import path
from . import views
app_name = "accounts"
urlpatterns = [
    path("signup/", views.signup,name="signup"), # 원가입
    # login
    path("login/", views.login,name="login"), # 원가입
    # logout
]
