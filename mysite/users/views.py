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
