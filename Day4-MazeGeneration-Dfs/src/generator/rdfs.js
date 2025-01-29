import { CellConfig } from "./cell";

function removeWalls(current, next) {
  const dx = current.x - next.x;
  const dy = current.y - next.y;

  if (dy === 1) {
    // Current is to the right of next
    current.borders.left = false;
    next.borders.right = false;
  } else if (dy === -1) {
    // Current is to the left of next
    current.borders.right = false;
    next.borders.left = false;
  }

  if (dx === 1) {
    // Current is below next
    current.borders.top = false;
    next.borders.bottom = false;
  } else if (dx === -1) {
    // Current is above next
    current.borders.bottom = false;
    next.borders.top = false;
  }
}

function checkCell(x, y, grid) {
  const rows = grid.length;
  const cols = grid[0].length;
  if (x < 0 || x >= rows || y < 0 || y >= cols) return null;
  return grid[x][y];
}

export default function generateMaze(grid) {
    // Deep copy the grid, preserving all properties
    const newGrid = grid.map((row) =>
      row.map((cell) => {
        const newCell = new CellConfig(cell.x, cell.y);
        newCell.borders = { ...cell.borders }; // Copy walls
        newCell.visited = cell.visited; // Copy visited status
        newCell.solution = cell.solution; // Copy solution status
        return newCell;
      })
    );
  
    const stack = []; // Stack for backtracking
    const solution = []; // Array to track the solution path
    let isSolving = true; // Flag to track if we're still solving
  
    let currentCell = newGrid[0][0]; // Start at the top-left cell
    solution.push(currentCell);
    while (true) {
      currentCell.visited = true;
  
      // Find a random unvisited neighbor
      const nextCell = currentCell.checkNeighbors((x, y) =>
        checkCell(x, y, newGrid)
      );
  
      if (nextCell) {
        // Push the current cell to the stack
        stack.push(currentCell);
  
        // Mark the next cell as visited
        nextCell.visited = true;
  
        // Remove walls between currentCell and nextCell
        removeWalls(currentCell, nextCell);
  
        // Move to the next cell
        currentCell = nextCell;
  
        // Add to solution path if still solving
        if (isSolving) solution.push(currentCell);
      } else if (stack.length > 0) {
        // If no unvisited neighbors, backtrack
  
        // Stop adding to solution path once the end is reached
        if (
          currentCell.x === newGrid.length - 1 &&
          currentCell.y === newGrid[0].length - 1
        ) {
          isSolving = false;
        }
  
        // Remove from solution path if backtracking
        if (isSolving) solution.pop();
  
        // Backtrack to the previous cell
        currentCell = stack.pop();
      } else {
        // If the stack is empty, we're done
        break;
      }
    }
  
    return [newGrid, solution];
  }