from django.views.generic import View, ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from django.contrib import messages
from users.models import User
from . import models, forms

class HomeView(ListView):

    model = models.Ware
    paginate_by = 6
    ordering = "created"
    context_object_name = "wares"


class WareDetail(DetailView):

    template_name = "wares/detail.html"
    model = models.Ware
    context_object_name = "ware"


class WareCreate(CreateView):
    form_class = forms.WareForm
    # model = models.Ware
    # context_object_name = "wares"
    template_name = "wares/create.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        ware = form.save()
        user = User.objects.get(username=self.request.user)
        ware.seller_id = user.id
        ware.save()
        messages.success(self.request, "물품이 등록되었습니다.")
        return redirect(reverse("home"))

    def form_invalid(self, form):         
        return super().form_invalid(form)

class SearchView(View):

    def get(self, request):

        city = request.GET.get("city")
        name = request.GET.get("name")
        print(name)

        if city or name:

            form = forms.SearchForm(request.GET)

            if form.is_valid():
                
                city = form.cleaned_data.get("city")
                name = form.cleaned_data.get("name")
                # price = form.cleaned_data.get("price")
                # seller = form.cleaned_data.get("seller")
                # categories = form.cleaned_data.get("category")

                filter_args = {}

                if city != "모든지역":
                    filter_args["city__startswith"] = city

                if name is not None:
                    filter_args["name__startswith"] = name

                # if price is not None:
                #     filter_args["price__lte"] = price

                # if seller is not None:
                #     filter_args["seller__startswith"] = seller
                
                # for category in categories:
                #     filter_args["category"] = category

                qs = models.Ware.objects.filter(**filter_args).order_by("-created")
                
                paginator = Paginator(qs, 4)
                page = request.GET.get("page", 1)
                wares = paginator.get_page(page)

                return render(
                    request, "wares/search.html", {"form": form, "wares": wares}
                )

        else:
            form = forms.SearchForm()

        return render(
                    request, "wares/search.html", {"form": form}
                )


    