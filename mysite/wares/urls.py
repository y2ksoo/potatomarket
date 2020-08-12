from django.urls import path
from . import views

app_name = "wares"

urlpatterns = [
    path("<int:pk>/", views.WareDetail.as_view(), name="detail"),
    path("add/", views.WareCreate.as_view(), name="create"),
    path("search/", views.SearchView.as_view(), name="search"),
]
