from django.urls import path

from . import views

urlpatterns = [
    path("search_all", views.search_all, name="search_all"),
    path("dijkstra", views.dijkstra, name="dijkstra"),
    path("a_star", views.a_star, name="a_star"),
]