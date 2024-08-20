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
visited = []

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
    start_position = search_initial("O")
    queue = []
    queue.append([start_position, [start_position]])
    
    while(queue!=[]):
        cel, path = queue.pop(0)
        neighbours = get_neighbours(cel[0], cel[1])

        for neighbour in neighbours:
            if(maze[neighbour[0]][neighbour[1]]=="X"):
                return path

            if(neighbour not in visited):
                new_path = path + [neighbour]                
                queue.append([neighbour, new_path])
                visited.append(neighbour)

solved_maze = []
solution = pathfinding()

for row in range(len(maze)):
    solved_maze_row = []
    for column in range(len(maze[row])):
        if([row, column] in solution):
            solved_maze_row.append('|')
        else:
            solved_maze_row.append(maze[row][column])
    solved_maze.append(solved_maze_row)


        

