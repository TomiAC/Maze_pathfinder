from django.shortcuts import render
from django.http import HttpResponse
from .dijkstra import *
from .a_star import *
from .dfs import *
from .bfs import *
from .mazes import define_maze


# Create your views here.
def index(request):
    return render(request, 'index.html')

def bfs(request):
    maze = define_maze()
    algorithm = 'Breadth-First Search'
    bd_template = 'bd_template1'
    url_vista = 'bfs'
    initial_celd = search_cell_coords_by_symbol("O", maze)
    solution, roads = solve_bfs(maze)
    
    roads.remove(initial_celd)
    solution.remove(initial_celd)

    return render(request, 'mazes.html', {'maze': maze, 'solution': solution, 'roads': roads, 'algorithm': algorithm, 'bd_template': bd_template, 'url_vista': url_vista})


def dijkstra(request):
    maze = define_maze()
    algorithm = 'Dijkstra'
    bd_template = 'bd_template2'
    url_vista = 'dijkstra'
    initial_celd = search_cell_coords_by_symbol("O", maze)
    solution, roads = shortest_path_dijkstra(maze)
    solution.reverse()

    solution.remove(initial_celd)
    roads.remove(initial_celd)

    return render(request, 'mazes.html', {'maze': maze, 'solution': solution, 'roads': roads, 'algorithm': algorithm, 'bd_template': bd_template, 'url_vista': url_vista})


def a_star(request):
    maze = define_maze()
    algorithm = 'A* Star'
    bd_template = 'bd_template3'
    url_vista = 'a_star'
    initial_celd = search_cell_coords_by_symbol("O", maze)
    solution, roads = shortest_path_a_star(maze)
    
    solution.remove(initial_celd)
    roads.remove(initial_celd)

    return render(request, 'mazes.html', {'maze': maze, 'solution': solution, 'roads': roads, 'algorithm': algorithm, 'bd_template': bd_template, 'url_vista': url_vista})

def dfs(request):
    maze = define_maze()
    algorithm = 'Deep-First Search'
    bd_template = 'bd_template4'
    url_vista = 'dfs'
    initial_celd = search_cell_coords_by_symbol("O", maze)
    solution, roads = path_dfs(maze)

    solution.remove(initial_celd)
    roads.remove(initial_celd)

    return render(request, 'mazes.html', {'maze': maze, 'solution': solution, 'roads': roads, 'algorithm': algorithm, 'bd_template': bd_template, 'url_vista': url_vista})