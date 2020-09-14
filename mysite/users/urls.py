from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.UserLoginView.as_view(), name="login"),
    path("login/kakao", views.kakao_login, name="kakao-login"),
    path("login/kakao/callback", views.kakao_callback, name="kakao-callback"),
    path("logout", views.log_out, name="logout"),
    path("signup", views.SignupView.as_view(), name="signup"),
]
