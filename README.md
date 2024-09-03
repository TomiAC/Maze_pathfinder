# Maze pathfinder
  This project is about a web aplication that allow the user to see how 4 different search algorithms work, trying to find a path thru the maze from the Start to the Finish.
The 4 used algorithms are:
### Breadth-First Search
  It begins the search at the Start Cell and explores all cells at the present depth prior to moving on to the cells at the next depth level.
### Depth-First Search
  It explores all paths in depth, going on the path as long as it can go or until de Finish, before exploring the next posible path.
### Dijkstra
  It is designed to find the shortest path from the Start Cell to all the cells in the maze. It takes into acount the cost of moving from one cell to another, considering the cost of the entire path to get to the specific cell.
  The cost of moving from one cell to all of its neighbours in the maze is one, so in this particular case, Djikstra works similar to BFS.
### A* Star
  The A* algorithm finds the shortest path by combining the actual cost from the start to a node g with an estimated cost to the goal h. Then it prioritizing those with the lowest total estimated cost f = g + h.
  For this case, the estimated cost is calculated as the direct distance from the cell to the Finish Cell, without considering all the obstacles in between.

# How it works
  As its a web app, its build with Django. Theres also a bit of Javascript for the dynamic visualization of how the maze is solved.
  The maze is presented as a 2D list of characters, where each character have a diferent meaning. This list are fixed so theres no way to change it.
  Then the maze is solved depending on which algorithm is choosen by the user.

# Examples
![image](https://github.com/user-attachments/assets/b57bac96-9b88-4a3e-bede-a9f47cc961d6)
![image](https://github.com/user-attachments/assets/54febc01-a643-43f9-bf1d-834666557760)
![image](https://github.com/user-attachments/assets/ae62a7cd-0ddc-4710-a9fa-b39a8a163136)
![image](https://github.com/user-attachments/assets/2822bd3b-3556-424b-b028-617ca3dca60c)


  
