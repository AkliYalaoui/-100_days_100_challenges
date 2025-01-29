import { v4 as uuidv4 } from 'uuid';

class CellConfig {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.key = uuidv4();
    this.borders = { top: true, left: true, bottom: true, right: true };
    this.visited = false;
    this.solution = false;
  }

  // Choose randomly one of the unvisited neighbors
  checkNeighbors(checkCell) {
    const neighbors = [];
    const top = checkCell(this.x, this.y - 1);
    const left = checkCell(this.x - 1, this.y);
    const bottom = checkCell(this.x, this.y + 1);
    const right = checkCell(this.x + 1, this.y);

    if (top && !top.visited) neighbors.push(top);
    if (left && !left.visited) neighbors.push(left);
    if (bottom && !bottom.visited) neighbors.push(bottom);
    if (right && !right.visited) neighbors.push(right);

    if (neighbors.length > 0) {
      const randomIndex = Math.floor(Math.random() * neighbors.length);
      return neighbors[randomIndex];
    }
    return false;
  }
}

export { CellConfig };