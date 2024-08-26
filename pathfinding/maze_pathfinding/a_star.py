from .utils import search_initial, search_final, get_neighbours, shortest_path, get_roads, maze
from operator import attrgetter
import time

class Cell_A_Star:

    def __init__(self, row, column, h):
        self.row = row
        self.column = column
        self.f = float("inf")
        self.g = float("inf")
        self.h = h
        self.parent = None

def calc_h(row_cell, column_cell, row_final, column_final):
    return (abs(row_cell - row_final)+abs(column_cell-column_final))

def search_final_a_star(final_symbol):
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if(maze[row][column]==final_symbol):
                cel = [row, column]
                return cel

def a_star_solve():
    lista_abiertos = []
    lista_cerrados = []
    list_of_cells = []

    start_position = search_initial("O")
    final_position = search_final_a_star("X")

    first_cell = Cell_A_Star(start_position[0], start_position[1], calc_h(start_position[0],start_position[1],final_position[0],final_position[1]))
    lista_abiertos.append(first_cell)
    list_of_cells.append(first_cell)

    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if((maze[row][column]!="#") & (maze[row][column]!="O")):
                list_of_cells.append(Cell_A_Star(row, column, calc_h(row, column,final_position[0],final_position[1])))

    while(lista_abiertos!=[]):
        cell = lista_abiertos.pop(lista_abiertos.index(min(lista_abiertos, key=attrgetter('f'))))
        neighbours = get_neighbours(cell.row, cell.column)
        lista_cerrados.append(cell)
        print(f'Fila: {cell.row}, Columna: {cell.column}, Parent: {cell.parent}')
        

        if(cell.row==final_position[0] and cell.column==final_position[1]):
            return lista_cerrados

        for neighbour in neighbours:

            for aux_neighbour in list_of_cells:
                if(aux_neighbour.row==neighbour[0] and aux_neighbour.column==neighbour[1]):
                    current_neighbour = aux_neighbour

            if(current_neighbour not in lista_abiertos and current_neighbour not in lista_cerrados):
                current_neighbour.g = cell.g + 1
                current_neighbour.f = current_neighbour.g + current_neighbour.h
                current_neighbour.parent = cell
                lista_abiertos.append(current_neighbour)
            
            if(current_neighbour in lista_abiertos and current_neighbour not in lista_cerrados):
                temp_distance = cell.g + 1
                if(temp_distance<current_neighbour.g):
                    current_neighbour.g = temp_distance
                    current_neighbour.f = temp_distance + current_neighbour.h
                    current_neighbour.parent = cell
    return 0

def get_roads_a_star(a_star_solved):
    roads_aux = sorted(a_star_solved, key=lambda cell: cell.g)
    roads = []
    for cell in roads_aux:
        if(maze[cell.row][cell.column]!='X'):
            roads.append([cell.row, cell.column])
    return roads

def shortest_path_a_star():
    a_star_solved = a_star_solve()
    shortest_path_for_a_star = shortest_path(search_final(a_star_solved))
    roads = get_roads_a_star(a_star_solved)
    return shortest_path_for_a_star, roads



        

    