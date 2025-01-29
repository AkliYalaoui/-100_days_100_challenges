import React from "react";

const Explanation = () => {
  return (
    <section className="my-8 md:my-12 p-4 md:p-6 bg-gray-50 rounded-lg shadow-md">
      <h2 className="text-2xl md:text-3xl text-center font-bold mb-4 md:mb-6 text-purple-700">
        How It Works
      </h2>

      <div className="space-y-4 md:space-y-6">
        {/* Step 1 */}
        <div>
          <h3 className="text-lg md:text-xl font-semibold mb-2 text-gray-800">
            1. Initialize the Grid
          </h3>
          <p className="text-sm md:text-base text-gray-600">
            The maze is represented as a 2D grid of cells. Each cell has four walls (top, bottom, left, right) and starts as unvisited.
          </p>
          <pre className="bg-gray-800 text-white p-3 md:p-4 rounded-md mt-2 overflow-x-auto">
            <code className="text-xs md:text-sm">
              {`Create a grid of size ROWS x COLS
For each cell in the grid:
  - Initialize all walls as "closed"
  - Mark the cell as "unvisited"`}
            </code>
          </pre>
        </div>

        {/* Step 2 */}
        <div>
          <h3 className="text-lg md:text-xl font-semibold mb-2 text-gray-800">
            2. Start at the Initial Cell
          </h3>
          <p className="text-sm md:text-base text-gray-600">
            The algorithm begins at the starting cell (usually the top-left corner of the grid).
          </p>
          <pre className="bg-gray-800 text-white p-3 md:p-4 rounded-md mt-2 overflow-x-auto">
            <code className="text-xs md:text-sm">
              {`Set the current cell as the starting cell (0, 0)
Mark the current cell as "visited"`}
            </code>
          </pre>
        </div>

        {/* Step 3 */}
        <div>
          <h3 className="text-lg md:text-xl font-semibold mb-2 text-gray-800">
            3. Explore Neighbors
          </h3>
          <p className="text-sm md:text-base text-gray-600">
            From the current cell, randomly select an unvisited neighbor. If a valid neighbor is found, move to that cell and remove the wall between the current cell and the neighbor.
          </p>
          <pre className="bg-gray-800 text-white p-3 md:p-4 rounded-md mt-2 overflow-x-auto">
            <code className="text-xs md:text-sm">
              {`While there are unvisited cells:
  - Find all unvisited neighbors of the current cell
  - If there are unvisited neighbors:
      - Randomly select one neighbor
      - Remove the wall between the current cell and the selected neighbor
      - Move to the selected neighbor
      - Mark the neighbor as "visited"
      - Push the current cell to the stack (for backtracking)`}
            </code>
          </pre>
        </div>

        {/* Step 4 */}
        <div>
          <h3 className="text-lg md:text-xl font-semibold mb-2 text-gray-800">
            4. Backtracking
          </h3>
          <p className="text-sm md:text-base text-gray-600">
            If the current cell has no unvisited neighbors, backtrack to the previous cell using the stack and continue the process.
          </p>
          <pre className="bg-gray-800 text-white p-3 md:p-4 rounded-md mt-2 overflow-x-auto">
            <code className="text-xs md:text-sm">
              {`If no unvisited neighbors are found:
  - Pop a cell from the stack
  - Set the popped cell as the current cell
  - Repeat the process`}
            </code>
          </pre>
        </div>

        {/* Step 5 */}
        <div>
          <h3 className="text-lg md:text-xl font-semibold mb-2 text-gray-800">
            5. Termination
          </h3>
          <p className="text-sm md:text-base text-gray-600">
            The algorithm terminates when all cells have been visited, and the stack is empty. The final grid represents the generated maze.
          </p>
          <pre className="bg-gray-800 text-white p-3 md:p-4 rounded-md mt-2 overflow-x-auto">
            <code className="text-xs md:text-sm">
              {`When the stack is empty and all cells are visited:
  - The maze generation is complete`}
            </code>
          </pre>
        </div>

        {/* Step 6 */}
        <div>
          <h3 className="text-lg md:text-xl font-semibold mb-2 text-gray-800">
            6. Solution Path (Optional)
          </h3>
          <p className="text-sm md:text-base text-gray-600">
            While generating the maze, the algorithm can also track the solution path from the start to the end cell.
          </p>
          <pre className="bg-gray-800 text-white p-3 md:p-4 rounded-md mt-2 overflow-x-auto">
            <code className="text-xs md:text-sm">
              {`While exploring:
  - If the current cell is the end cell:
      - Mark the path as the solution
  - If backtracking:
      - Remove the last cell from the solution path`}
            </code>
          </pre>
        </div>
      </div>
    </section>
  );
};

export default Explanation;