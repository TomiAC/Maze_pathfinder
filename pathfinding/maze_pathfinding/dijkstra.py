from .utils import *
from operator import attrgetter

class Cell:
    '''
    Cell class for the Dijkstra algorithm

    Attributes:
        row (int): Row of the cell in the maze.
        column (int): Column og the cell in the maze.
        distance (int): The distance from the beginning to this cell
        parent (Cell): The previous cell.
    '''

    def __init__(self, row, column, distance=float("inf")) -> None:
        self.row = row
        self.column = column
        self.distance = distance
        self.parent = None


def search_final(visited:list[Cell]):
    '''
    Returns the final cell of the list of visited.

    Parameters:
        visited (list(Cell)): List of visited cells.

    Returns:
        cell (Cell): The final cell of the visited list.

    '''
    for cell in visited:
        if(maze[cell.row][cell.column] == 'X'):
            return cell
        

def shortest_path(cell):
    '''
    Get a list of the pair file, column of the cells that are in the path to the finish.

    Parameters
        cell Cell: The final cell.
    
    Returns
        solution list(list(int)): A list of the file and column of the cells.

    '''
    solution = []
    aux = cell.parent
    while(aux is not None):
        solution.append([aux.row, aux.column])
        aux = aux.parent
    return solution


def get_roads(visited):
    '''
    Get a list of the pair file, column of the cells that are in the analised roads.

    Parameters
        visited list(Cell): The list of all the visited cells.
    
    Returns
        roads list(list(int)): A list of the file and column of the cells.
    '''
    roads_aux = sorted(visited, key=lambda cell: cell.distance)
    roads = []
    for cell in roads_aux:
        if(maze[cell.row][cell.column]!='X'):
            roads.append([cell.row, cell.column])
    return roads

    
def shortest_path_dijkstra():
    '''
    Make a list of the pair file, column of the shortest path and the cells visited to be presented in the HTML Table.

    Returns
        shortest_path_dij list(list(int)): A list of the cells that form the path from the beginning to the finish.
        roads list(list(int)): A list of all the cells that where considered during the process.
    '''
    visited = solve_dijkstra()
    shortest_path_dij = shortest_path(search_final(visited))
    roads = get_roads(visited)
    return shortest_path_dij, roads


def solve_dijkstra():
    '''
    Find the shortest past in the maze using the Djikstra algorithm.

    Returns
        visited list(Cell): List of all the visited cells or 0 if not path was found.
    '''
    visited = set()
    star_position = search_cell_coords_by_symbol("O")
    first_cell = Cell(star_position[0], star_position[1], distance=0)

    list_of_cells = []
    list_of_cells.append(first_cell)

    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if((maze[row][column]!="#") & (maze[row][column]!="O")):
                list_of_cells.append(Cell(row, column))
    
    visited.add(first_cell)

    while(list_of_cells!=[]):
        cell = list_of_cells.pop(list_of_cells.index(min(list_of_cells, key=attrgetter('distance'))))
        neighbours = get_neighbours(cell.row, cell.column)

        for neighbour in neighbours:
            for aux_neighbour in list_of_cells:
                if(aux_neighbour.row==neighbour[0] and aux_neighbour.column==neighbour[1]):
                    current_neighbour = aux_neighbour
            
            if(maze[current_neighbour.row][current_neighbour.column]=='X'):
                current_distance = cell.distance + 1
                visited.add(current_neighbour)
                list_of_cells[list_of_cells.index(current_neighbour)].distance = current_distance
                list_of_cells[list_of_cells.index(current_neighbour)].parent = cell
                return visited

            if(current_neighbour not in visited):
                current_distance = cell.distance + 1
                if(current_neighbour.distance > current_distance):
                    visited.add(current_neighbour)
                    list_of_cells[list_of_cells.index(current_neighbour)].distance = current_distance
                    list_of_cells[list_of_cells.index(current_neighbour)].parent = cell
    return 0
