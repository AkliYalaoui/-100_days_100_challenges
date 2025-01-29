import { useState } from "react";
import generateMaze from "../generator/rdfs";
import { CellConfig } from "../generator/cell";
import Cell from "./Cell";

const Maze = () => {
  const nRows = 20;
  const nCols = 20;

  // Initialize the grid
  const initialGrid = Array.from({ length: nRows }, (_, r) =>
    Array.from({ length: nCols }, (_, c) => new CellConfig(r, c))
  );

  const [M, setM] = useState(initialGrid);
  const [answerEnabled, setAnswerEnabled] = useState(false);
  const [answer, setAnswer] = useState([]);

  // Function to reset the maze to its initial state
  const restartMaze = () => {
    setM(initialGrid);
    setAnswerEnabled(false);
    setAnswer([]);
  };

  return (
    <main className="container m-auto mb-8 md:mb-18 p-2 md:p-4 flex justify-center items-center flex-col">
      {/* Maze Grid */}
      <div
        className="grid gap-0 place-items-stretch"
        style={{
          gridTemplateRows: `repeat(${nRows}, minmax(10px, 20px))`,
          gridTemplateColumns: `repeat(${nCols}, minmax(10px, 20px))`,
        }}
      >
        {M.map((row) =>
          row.map((cell) => (
            <Cell key={cell.key} config={cell} ncols={nCols} nrows={nRows} />
          ))
        )}
      </div>

      {/* Buttons */}
      <div className="flex flex-col md:flex-row space-y-2 md:space-y-0 md:space-x-4 my-4">
        <button
          onClick={() => {
            const [newM, Answer] = generateMaze(M);
            setAnswer(Answer);
            setAnswerEnabled(true);
            setM(newM);
          }}
          className="p-2 bg-purple-500 rounded text-white hover:bg-purple-600 transition-colors text-sm md:text-base"
        >
          Generate Maze
        </button>
        {answerEnabled && (
          <>
            <button
              onClick={() => {
                setM((prevM) =>
                  prevM.map((row) =>
                    row.map((cell) => {
                      if (answer.includes(cell)) {
                        return { ...cell, solution: true };
                      }
                      return cell;
                    })
                  )
                );
              }}
              className="p-2 bg-green-500 rounded text-white hover:bg-green-600 transition-colors text-sm md:text-base"
            >
              Show Solution
            </button>
            <button
              onClick={restartMaze}
              className="p-2 bg-red-500 rounded text-white hover:bg-red-600 transition-colors text-sm md:text-base"
            >
              Restart
            </button>
          </>
        )}

      </div>
    </main>
  );
};

export default Maze;