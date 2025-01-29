# Day4-MazeGeneration-Dfs

This project implements a **maze generation algorithm** using the **Iterative Backtracking** approach. The maze is generated on a grid, and the algorithm also finds a solution path from the start to the end of the maze.

## Features

- **Maze Generation**: Generates a random maze using the Recursive Backtracking algorithm.
- **Solution Path**: Finds a path from the start (top-left corner) to the end (bottom-right corner) of the maze.
- **Interactive Visualization**: Displays the maze and the solution path in a clean and intuitive format.

## How It Works

### Algorithm Overview

1. **Initialize the Grid**:
   - Create a 2D grid of cells, where each cell has four walls (top, bottom, left, right).
   - Mark all cells as unvisited.

2. **Start at the Initial Cell**:
   - Begin at the top-left corner of the grid (cell `[0, 0]`).

3. **Explore Neighbors**:
   - Randomly select an unvisited neighbor of the current cell.
   - Remove the wall between the current cell and the selected neighbor.
   - Move to the selected neighbor and mark it as visited.
   - Repeat the process until all cells are visited.

4. **Backtracking**:
   - If a cell has no unvisited neighbors, backtrack to the previous cell using a stack.
   - Continue the process until the stack is empty.

5. **Solution Path**:
   - While generating the maze, track the path from the start to the end cell.
   - Once the end cell is reached, the solution path is finalized.

### Code Structure

- **`cell.js`**: Defines the `CellConfig` class, which represents a cell in the grid.
- **`generateMaze.js`**: Implements the maze generation algorithm.
- **`Maze.jsx`**: Renders the maze and the solution path using React.

### Example
Here’s an example of a generated maze:

+---+---+---+---+---+
| S |   |       |   |
+   +   +---+   +   +
|   |   |       |   |
+   +---+   +---+   +
|           |       |
+   +---+   +---+   +
|   |       |       |
+   +   +---+   +   +
| E |           |   |
+---+---+---+---+---+

### Pseudo Code
Here’s the high-level pseudo code for the maze generation algorithm:
1. Initialize a grid of cells with all walls intact.
2. Start at the initial cell (0, 0).
3. While there are unvisited cells:
   a. Find a random unvisited neighbor.
   b. Remove the wall between the current cell and the neighbor.
   c. Move to the neighbor and mark it as visited.
   d. Push the current cell to the stack.
4. If no unvisited neighbors are found:
   a. Backtrack to the previous cell using the stack.
5. Repeat until all cells are visited.