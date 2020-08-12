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

    # def form_valid(self, form):
    #     form.save()
    #     username = form.cleaned_data.get("username")
    #     password = form.cleaned_data.get("password")
    #     user = authenticate(self.request, username=username, password=password)
    #     if user is not None:
    #         login(self.request, user)
    #     return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("home")
 
    #     print("hello valid")
    #     username = form.cleaned_data.get("username")
    #     password = form.cleaned_data.get("password")
    #     user = authenticate(self.request, username=username, password=password)
    #     if user is not None:
    #         print("hello login")
    #         login(self.request, user)
    #     return super().form_valid(form)

def log_out(request):
    logout(request)
    return redirect(reverse("home"))




