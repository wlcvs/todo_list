from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListListView, name="index"),
    path("list/<int:list_id>/",
         viewd.ItemListview, name="list"),
]
