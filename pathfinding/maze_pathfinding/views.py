from django.shortcuts import render
from django.http import HttpResponse
from .utils import *


# Create your views here.
def search_all(request):
    initial_celd = search_initial("O")
    solution, roads = solve_search_all()
    
    roads.remove(initial_celd)
    solution.remove(initial_celd)
    return render(request, 'search_all.html', {'maze': maze, 'solution': solution, 'roads': roads})

def dijkstra(request):
    hola = solve_dijkstra()
    return render(request, 'dijkstra.html', {'maze': maze})