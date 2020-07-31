from django.urls import path
from . import views

app_name = "wares"

urlpatterns = [
    path("<int:pk>", views.WareDetail.as_view(), name="detail"),
    path("add", views.WareCreate.as_view(), name="create"),
    path("add2", views.CreateWare.as_view(), name="create2"),
]
