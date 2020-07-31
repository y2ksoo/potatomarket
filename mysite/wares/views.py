from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from . import models, forms

class HomeView(ListView):

    model = models.Ware
    paginate_by = 20
    ordering = "created"
    context_object_name = "wares"


class WareDetail(DetailView):

    template_name = "wares/detail.html"
    model = models.Ware
    context_object_name = "ware"


class WareCreate(CreateView):
    model = models.Ware
    template_name = "wares/create.html"
    fields = ['name', 'description', 'price', 'city', 'seller', 'category']
    success_url = reverse_lazy("home")


class CreateWare(FormView):

    template_name = "wares/create2.html"
    form_class = forms.WareForm
    success_url = reverse_lazy("home")
    
    def form_invalid(self, form):
        print("Error!")
        print(form.error)

    def form_vaild(self, form):
        print(form.cleaned_data)
        form.save()
        return super().form_valid(form)
    