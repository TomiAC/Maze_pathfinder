from .utils import search_cell_coords_by_symbol, get_neighbours, maze
from .dijkstra import search_final, shortest_path
from operator import attrgetter

class Cell_A_Star:
    '''
    Cell class for the Dijkstra algorithm

    Attributes:
        row (int): Row of the cell in the maze.
        column (int): Column og the cell in the maze.
        f (int): f = g + h.
        g (int): The distance from the beginning to this cell.
        h (int): The direct distance from this cell to the finish.
        parent (Cell): The previous cell.
    '''

    def __init__(self, row, column, h, g=float("inf")):
        self.row = row
        self.column = column
        self.f = g + h
        self.g = g
        self.h = h
        self.parent = None

def calc_h(row_cell, column_cell, row_final, column_final):
    '''
    Calculate the direct distance from the cell to the finish.
    
    Parameters
        row_cell (int): The row of the cell.
        column_cell (int): The column of the cell.
        row_final (int): The row of the finish.
        column_final (int): The column of the finish.
    
    Returns
        _ (int): The direct distance from the cell to the finish.
    '''
    return (abs(row_cell - row_final)+abs(column_cell-column_final))

def get_roads_a_star(a_star_solved):
    '''
    Get a list of the pair file, column of the cells that are in the analised roads.

    Parameters
        a_star_solved list(Cell_A_Star): The list of all the visited cells.
    
    Returns
        roads list(list(int)): A list of the file and column of the cells.
    '''
    roads_aux = sorted(a_star_solved, key=lambda cell: cell.g)
    roads = []
    for cell in roads_aux:
        if(maze[cell.row][cell.column]!='X'):
            roads.append([cell.row, cell.column])
    return roads

def shortest_path_a_star():
    '''
    Make a list of the pair file, column of the shortest path and the cells visited to be presented in the HTML Table.

    Returns
        shortest_path_for_a_star list(list(int)): A list of the cells that form the path from the beginning to the finish.
        roads list(list(int)): A list of all the cells that where considered during the process.
    '''
    a_star_solved = a_star_solve()
    shortest_path_for_a_star = shortest_path(search_final(a_star_solved))
    roads = get_roads_a_star(a_star_solved)
    return shortest_path_for_a_star, roads

def a_star_solve():
    '''
    Find the shortest past in the maze using the A* Star algorithm.

    Returns
        closed_list list(Cell_A_Star): List of all the visited cells or 0 if not path was found.
    '''
    open_list = []
    closed_list = []
    list_of_cells = []

    start_position = search_cell_coords_by_symbol("O")
    final_position = search_cell_coords_by_symbol("X")

    first_cell = Cell_A_Star(start_position[0], start_position[1], calc_h(start_position[0],start_position[1],final_position[0],final_position[1]), g=0)
    open_list.append(first_cell)
    list_of_cells.append(first_cell)

    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if((maze[row][column]!="#") & (maze[row][column]!="O")):
                list_of_cells.append(Cell_A_Star(row, column, calc_h(row, column,final_position[0],final_position[1])))

    while(open_list!=[]):
        cell = open_list.pop(open_list.index(min(open_list, key=attrgetter('f'))))
        neighbours = get_neighbours(cell.row, cell.column)
        if(cell.parent is not None):
            cell.g = cell.parent.g + 1
            cell.f = cell.g + cell.h
        closed_list.append(cell)
        

        if(cell.row==final_position[0] and cell.column==final_position[1]):
            return closed_list

        for neighbour in neighbours:

            for aux_neighbour in list_of_cells:
                if(aux_neighbour.row==neighbour[0] and aux_neighbour.column==neighbour[1]):
                    current_neighbour = aux_neighbour

            if(current_neighbour not in open_list and current_neighbour not in closed_list):
                current_neighbour.g = cell.g + 1
                current_neighbour.f = current_neighbour.g + current_neighbour.h
                current_neighbour.parent = cell
                open_list.append(current_neighbour)
            
            if(current_neighbour in open_list and current_neighbour not in closed_list):
                temp_distance = cell.g + 1
                if(temp_distance<current_neighbour.g):
                    current_neighbour.g = temp_distance
                    current_neighbour.f = temp_distance + current_neighbour.h
                    current_neighbour.parent = cell
    return 0



        

    