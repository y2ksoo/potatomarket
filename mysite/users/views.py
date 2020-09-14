import os
import requests
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView
from . import forms, models


class SignupView(CreateView):
    model = get_user_model()
    form_class = forms.SignUpForm
    template_name = "users/signup.html"    
    success_url = reverse_lazy("home")


class UserLoginView(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("home")
    

def log_out(request):
    logout(request)
    return redirect(reverse("home"))


def kakao_login(request):
    client_id = os.environ.get("KAKAO_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
    )


class KakaoException(Exception):
    pass


def kakao_callback(request):
    try:
        code = request.GET.get("code")
        client_id = os.environ.get("KAKAO_ID")
        redirect_uri = "http://127.0.0.1:8000/users/login/kakao/callback"
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
        )
        token_json = token_request.json()        
        error = token_json.get("error", None)
        if error is not None:
            raise KakaoException()
        access_token = token_json.get("access_token") 
        
        profile_request = requests.get(
            "https://kapi.kakao.com/v2/user/me", 
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        print(profile_json)

        username = profile_json.get("properties").get("nickname")
        if username is None:
            raise KakaoException()
        # print(username)
        try:
            user = models.User.objects.get(username=username)
            if user.login_method != models.User.LOGING_KAKAO:
                raise KakaoException()
        except models.User.DoesNotExist:
            print("Create New User %s", username)
            user = models.User.objects.create(
                username=username,
                first_name=username,
                login_method=models.User.LOGING_KAKAO,
            )
            user.set_unusable_password()
            user.save()

        print(user)
        login(request, user)
        return redirect(reverse_lazy("home"))

    except KakaoException:
        return redirect(reverse("users:login"))
