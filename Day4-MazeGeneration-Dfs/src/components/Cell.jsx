const Cell = ({ config, ncols, nrows }) => {
  const borderR = config.borders.right && (config.x + config.y) != (ncols + nrows - 2) ? "border-r border-gray-900" : "";
  const borderT = config.borders.top ? "border-t border-gray-900" : "";
  const borderL = config.borders.left && (config.x + config.y) > 0 ? "border-l border-gray-900" : "";
  const borderB = config.borders.bottom ? "border-b border-gray-900" : "";
  const color = config.solution ? "bg-green-300" : "bg-white";

  return (
    <div
      className={`w-5 h-5 flex items-center justify-center ${borderR} ${borderL} ${borderT} ${borderB} ${color}`}
    ></div>
  );
};

export default Cell;