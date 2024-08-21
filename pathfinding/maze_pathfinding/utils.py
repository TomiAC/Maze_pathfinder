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
        if(maze[row-1][column]!="#" & maze[row][column]!="O"):
           neighbours.append([row-1, column])
    if(row<(len(maze))-1):
        if(maze[row+1][column]!="#" & maze[row][column]!="O"):
           neighbours.append([row+1, column])
    if(column>0):
        if(maze[row][column-1]!="#" & maze[row][column]!="O"):
           neighbours.append([row, column-1])
    if(column<(len(maze[0]))-1):
        if(maze[row][column+1]!="#" & maze[row][column]!="O"):
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

def solve_dijkstra():
    visited = []
    star_position = search_initial("O")
    first_cell = {"row": star_position[0], "column": star_position[1], "distance": 0, "parent": None}

    list_of_cells = []
    list_of_cells.append(first_cell)

    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if((maze[row][column]!="#") & (maze[row][column]!="O") & (maze[row][column]!="X")):
                list_of_cells.append({"row": row, "column": column, "distance": float("inf"), "parent": 0})
    
    visited.append(first_cell)
    print(list_of_cells)

    while(list_of_cells!=[]):
        cell = list_of_cells.pop(list_of_cells.index(min(list_of_cells, key=lambda x: x["distance"])))
        neighbours = get_neighbours(cell["row"], cell["column"])

        for neighbour in neighbours:
            current_neighbour = list_of_cells[list_of_cells.index({"row": neighbour[0], "column": neighbour[1], "distance": float("inf"), "parent": 0})]
            if(current_neighbour not in visited):
                current_distance = cell["distance"] + 1
                if(current_neighbour["distance"] > current_distance):
                    list_of_cells[list_of_cells.index(current_neighbour)]["distance"] = current_distance
                    list_of_cells[list_of_cells.index(current_neighbour)]["parent"] = cell
    print(list_of_cells)
    return 0
    


        