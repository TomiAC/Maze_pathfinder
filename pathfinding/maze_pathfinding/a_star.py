from utils import search_initial, search_final, get_neighbours, maze
from operator import attrgetter

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

def a_star():
    lista_abiertos = []
    lista_cerrados = []

    start_position = search_initial("O")
    final_position = search_final()
    first_cell = Cell_A_Star(start_position[0], start_position[1], calc_h(start_position[0],start_position[1],final_position[0],final_position[1]))

    lista_abiertos.append(first_cell)

    while(lista_abiertos!=[]):
        cell = lista_abiertos.pop(lista_abiertos.index(min(lista_abiertos, key=attrgetter('f'))))
        neighbours = get_neighbours(cell.row, cell.column)
        lista_cerrados.append(cell)

        if(cell.row==final_position[0] and cell.column==final_position[1]):
            return lista_cerrados

        for neighbour in neighbours:
            for aux_neighbour in lista_abiertos:
                if(aux_neighbour.row==neighbour[0] and aux_neighbour.column==neighbour[1]):
                    current_neighbour = aux_neighbour
            
            if(current_neighbour not in lista_abiertos):
                current_neighbour.g = cell.g + 1
                current_neighbour.f = current_neighbour.g + current_neighbour.h
                current_neighbour.parent = cell
                lista_abiertos.append(current_neighbour)
            
            if(current_neighbour in lista_abiertos):
                temp_distance = cell.g + 1
                if(temp_distance<current_neighbour.g):
                    current_neighbour.g = temp_distance
                    current_neighbour.f = temp_distance + current_neighbour.h
                    current_neighbour.parent = cell
    print('Salio')
    print(lista_cerrados)


        

    