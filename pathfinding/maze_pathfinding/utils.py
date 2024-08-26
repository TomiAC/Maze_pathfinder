from operator import attrgetter

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", " ", "#", "#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", " ", "#", " ", "#", "#", " ", "#", "#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", "#", "#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", " ", "#", " ", "#", "#", " ", "#", "#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", " ", "#", " ", "#", "#", " ", "#", "#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", " ", "#", "#", "#", "#", " ", "#", "#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "X", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

class Cell:

    def __init__(self, row, column, distance=float("inf")):
        self.row = row
        self.column = column
        self.distance = distance
        self.parent = None


def search_initial(initial_symbol):
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if(maze[row][column]==initial_symbol):
                cel = [row, column]
                return cel
            

def search_final(visited):
    for cell in visited:
        if(maze[cell.row][cell.column] == 'X'):
            return cell


def get_neighbours(row, column):
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
    visited = []
    roads = []
    start_position = search_initial("O")
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


def shortest_path(cell):
    solution = []
    aux = cell.parent
    while(aux is not None):
        solution.append([aux.row, aux.column])
        aux = aux.parent
    return solution

def get_roads(visited):
    roads_aux = sorted(visited, key=lambda cell: cell.distance)
    roads = []
    for cell in roads_aux:
        if(maze[cell.row][cell.column]!='X'):
            roads.append([cell.row, cell.column])
    return roads


def solve_dijkstra():
    visited = set()
    star_position = search_initial("O")
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
    
def shortest_path_dijkstra():
    visited = solve_dijkstra()
    shortest_path_var = shortest_path(search_final(visited))
    roads = get_roads(visited)
    return shortest_path_var, roads