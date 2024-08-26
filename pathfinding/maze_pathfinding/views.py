from django.shortcuts import render
from django.http import HttpResponse
from .utils import *


# Create your views here.
def search_all(request):
    algorithm = 'Serch all paths'
    bd_template = 'bd_template1'
    initial_celd = search_initial("O")
    solution, roads = solve_search_all()
    
    roads.remove(initial_celd)
    solution.remove(initial_celd)
    return render(request, 'mazes.html', {'maze': maze, 'solution': solution, 'roads': roads, 'algorithm': algorithm, 'bd_template': bd_template})

def dijkstra(request):
    algorithm = 'Dijkstra'
    bd_template = 'bd_template2'
    initial_celd = search_initial("O")
    solution, roads = shortest_path_dijkstra()
    solution.reverse()
    solution.remove(initial_celd)
    roads.remove(initial_celd)
    return render(request, 'mazes.html', {'maze': maze, 'solution': solution, 'roads': roads, 'algorithm': algorithm, 'bd_template': bd_template})