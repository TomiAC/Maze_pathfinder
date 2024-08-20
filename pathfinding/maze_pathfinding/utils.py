maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def search_initial(initial_symbol):
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if(maze[row][column]==initial_symbol):
                cel = [row, column]
                return cel

def get_neighbours(row, column):
    neighbours = []
    if(row>0):
        if(maze[row-1][column]!="#"):
           neighbours.append([row-1, column])
    if(row<(len(maze))-1):
        if(maze[row+1][column]!="#"):
           neighbours.append([row+1, column])
    if(column>0):
        if(maze[row][column-1]!="#"):
           neighbours.append([row, column-1])
    if(column<(len(maze[0]))-1):
        if(maze[row][column+1]!="#"):
           neighbours.append([row, column+1])
    return neighbours

def pathfinding():
    visited=[]
    roads = []
    start_position = search_initial("O")
    queue = []
    queue.append([start_position, [start_position]])
    visited.append(start_position)
    roads.append(start_position)
    
    while(queue!=[]):
        cel, path = queue.pop(0)
        neighbours = get_neighbours(cel[0], cel[1])

        for neighbour in neighbours:
            if(maze[neighbour[0]][neighbour[1]]=="X"):
                return path, roads

            if(neighbour not in visited):
                roads.append(neighbour)
                new_path = path + [neighbour]                
                queue.append([neighbour, new_path])
                visited.append(neighbour)