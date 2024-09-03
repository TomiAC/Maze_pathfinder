from .utils import *

def solve_bfs(maze):
    '''
    Finds the path to the finish cell by looking all the posible roads.

    Returns
        path list(list(int)): A list of the cells that form the path from the beginning to the finish.
        roads list(list(int)): A list of all the cells that where considered during the process.
    '''
    visited = []
    roads = []
    start_position = search_cell_coords_by_symbol("O", maze)
    queue = []
    queue.append([start_position, [start_position]])
    visited.append(start_position)
    roads.append(start_position)
    
    while(queue!=[]):
        cell, path = queue.pop(0)
        neighbours = get_neighbours(cell[0], cell[1], maze)

        for neighbour in neighbours:
            if(maze[neighbour[0]][neighbour[1]]=="X"):
                return path, roads

            if(neighbour not in visited):
                roads.append(neighbour)
                new_path = path + [neighbour]                
                queue.append([neighbour, new_path])
                visited.append(neighbour)