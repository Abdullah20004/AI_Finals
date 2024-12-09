import tkinter as tk
from collections import deque
import time

# maze we want to have 
maze = [
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Maze dimensions
CELL_SIZE = 40
maze_height = len(maze)
maze_width = len(maze[0])

# Defining the start and end states
start = (0, 0)  
goal = (9, 9)   

# BFS function to find the shortest path
def bfs(maze, start, goal):
    queue = deque([(start, [start])])  # Queue holds (position, path)
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()

        # If the current cell is the goal then return  path
        if (x, y) == goal:
            return path

        # Check all four directions up, down, left and right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < maze_height and 0 <= ny < maze_width:
                if maze[nx][ny] == 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))

    return []  # Return an empty list if no path is found

# Initialize Tkinter window
window = tk.Tk()
window.title("Maze Game with BFS")
canvas = tk.Canvas(window, width=maze_width * CELL_SIZE, height=maze_height * CELL_SIZE)
canvas.pack()

# Draw the maze
def draw_maze():
    for row in range(maze_height):
        for col in range(maze_width):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            color = "black" if maze[row][col] == 1 else "white"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

            # Draw "S" at the starting position
            if (row, col) == start:
                canvas.create_text(x1 + CELL_SIZE // 2, y1 + CELL_SIZE // 2, text="S", font=("Arial", 20), fill="red")

            # Draw "E" at the goal position
            if (row, col) == goal:
                canvas.create_text(x1 + CELL_SIZE // 2, y1 + CELL_SIZE // 2, text="E", font=("Arial", 20), fill="green")

# Draw the player
def draw_player(position):
    x1 = position[1] * CELL_SIZE
    y1 = position[0] * CELL_SIZE
    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE
    return canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

# Move the player step-by-step through the path
def move_player(path, index=0, start_time=None):
    if start_time is None:
        start_time = time.time()  # Start timing the traversal

    if index < len(path):
        position = path[index]
        canvas.coords(player, position[1] * CELL_SIZE, position[0] * CELL_SIZE,
                       (position[1] + 1) * CELL_SIZE, (position[0] + 1) * CELL_SIZE)
        # Schedule the next move after 1 second (1000 ms)
        window.after(1000, move_player, path, index + 1, start_time)
    else:
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken to reach the goal: {time_taken:.2f} seconds")

# Run BFS search, draw the maze, and move the player
draw_maze()
path = bfs(maze, start, goal)
if path:
    player = draw_player(start)  # Draw player at the start position
    move_player(path)            # Start moving the player along the path
else:
    print("No path found")

window.mainloop()
