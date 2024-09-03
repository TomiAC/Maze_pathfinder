from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bfs", views.bfs, name="bfs"),
    path("dijkstra", views.dijkstra, name="dijkstra"),
    path("a_star", views.a_star, name="a_star"),
    path("dfs", views.dfs, name="dfs")
]