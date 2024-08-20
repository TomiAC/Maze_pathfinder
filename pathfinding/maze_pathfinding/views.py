from django.shortcuts import render
from django.http import HttpResponse
from .utils import *


# Create your views here.
def index(request):
    initial_celd = search_initial("O")
    solution, roads = pathfinding()
    roads.remove(initial_celd)
    solution.remove(initial_celd)
    return render(request, 'index.html', {'maze': maze, 'solution': solution, 'roads': roads})