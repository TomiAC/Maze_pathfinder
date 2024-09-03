from .utils import get_neighbours, search_cell_coords_by_symbol

class Cell_DFS():

    def __init__(self, row, column, parent) -> None:
        self.row = row
        self.column = column
        self.parent = parent

def solve_dfs(cell, visited, list_of_cells, maze, band):
    '''
    Finds the path to the finish cell by looking all the posible roads.

    Returns
        path list(list(int)): A list of the cells that form the path from the beginning to the finish.
        roads list(list(int)): A list of all the cells that where considered during the process.
    '''
    neighbours = get_neighbours(cell.row, cell.column, maze)

    for neighbour in neighbours:

        for aux_neighbour in list_of_cells:
            if(aux_neighbour.row==neighbour[0] and aux_neighbour.column==neighbour[1]):
                current_neighbour = aux_neighbour

        if(maze[neighbour[0]][neighbour[1]]=="X"):
            current_neighbour.parent = cell
            visited.append(current_neighbour)
            return True

        if(current_neighbour not in visited):
            current_neighbour.parent = cell
            visited.append(current_neighbour)
            if (solve_dfs(current_neighbour, visited, list_of_cells, maze, band)):
                return True

def path_dfs(maze):
    visited = []
    start_position = search_cell_coords_by_symbol("O", maze)
    first_cell = Cell_DFS(start_position[0], start_position[1], None)
    visited.append(first_cell)
    list_of_cells = []
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if((maze[row][column]!="#") & (maze[row][column]!="O")):
                list_of_cells.append(Cell_DFS(row, column, None))

    solve_dfs(first_cell, visited, list_of_cells, maze, False)
    final_cell = None
    aux_visited = []
    for cell in visited:
        if(maze[cell.row][cell.column] == 'X'):
            final_cell = cell
        else:
            aux_visited.append([cell.row, cell.column])
    solution = []
    aux = final_cell.parent
    while(aux is not None):
        solution.append([aux.row, aux.column])
        aux = aux.parent
    return solution, aux_visited

