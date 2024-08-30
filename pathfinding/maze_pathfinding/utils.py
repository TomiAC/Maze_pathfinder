from operator import attrgetter
from .mazes import *
import random

#Just a random choose of what maze is going to be shown
choosen_maze = random.randint(1,4)
if(choosen_maze==1):
    maze = maze1
elif choosen_maze ==2:
    maze = maze2
elif choosen_maze==3:
    maze = maze3
elif choosen_maze==4:
    maze = maze4


def search_cell_coords_by_symbol(symbol:str) -> list[int]:
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
            

def get_neighbours(row, column):
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


def solve_search_all():
    '''
    Finds the path to the finish cell by looking all the posible roads.

    Returns
        path list(list(int)): A list of the cells that form the path from the beginning to the finish.
        roads list(list(int)): A list of all the cells that where considered during the process.
    '''
    visited = []
    roads = []
    start_position = search_cell_coords_by_symbol("O")
    queue = []
    queue.append([start_position, [start_position]])
    visited.append(start_position)
    roads.append(start_position)
    
    while(queue!=[]):
        cell, path = queue.pop(0)
        neighbours = get_neighbours(cell[0], cell[1])

        for neighbour in neighbours:
            if(maze[neighbour[0]][neighbour[1]]=="X"):
                return path, roads

            if(neighbour not in visited):
                roads.append(neighbour)
                new_path = path + [neighbour]                
                queue.append([neighbour, new_path])
                visited.append(neighbour)