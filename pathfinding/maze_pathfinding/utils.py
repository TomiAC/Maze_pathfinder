from operator import attrgetter
from .mazes import *


#Just a random choose of what maze is going to be shown


def search_cell_coords_by_symbol(symbol:str, maze:list) -> list[int]:
    '''
    Search the file and column of the cell that contains the symbol passed as argument.

    Parameters:
        symbol (str): The symbol which is going to be looked for in the maze.

    Returns:
        cell (list(int)): Return a list of 2 positions, the first one is the file the second one is the column

    '''
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if(maze[row][column]==symbol):
                cell = [row, column]
                return cell
            

def get_neighbours(row, column, maze):
    '''
    Returns a list of all available neighbours of the cell in the row and column passed.

    Parameters:
        row (int): The row of the cell.
        column (int): The column of the cell.
    
    Returns:
        neighbours (list(list(int))): Returns a list with a list for every pair of file, column of every available neighbour.
    '''
    neighbours = []
    if(row>0):
        if((maze[row-1][column]!="#") and (maze[row-1][column]!="O")):
           neighbours.append([row-1, column])
    if(row<(len(maze))-1):
        if((maze[row+1][column]!="#") and (maze[row+1][column]!="O")):
           neighbours.append([row+1, column])
    if(column>0):
        if((maze[row][column-1]!="#") and (maze[row][column-1]!="O")):
           neighbours.append([row, column-1])
    if(column<(len(maze[0]))-1):
        if((maze[row][column+1]!="#") and (maze[row][column+1]!="O")):
           neighbours.append([row, column+1])
    return neighbours

def search_final(visited, maze):
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
