function spiralOrder(matrix: number[][]): number[] {
    let x = 0;
    let y = 0;
    const m = matrix.length;
    const n = matrix[0].length;

    let startX = 0;
    let endX = n - 1;
    let startY = 0;
    let endY = m - 1;
    let total = m * n;

    const result: number[] = [];
    while (startX <= endX && startY <= endY && total > 0) {
      for (let i = startX; i <= endX && total > 0; i++) {
        result.push(matrix[y][x]);
        x++;
        total--;
      }
      
      x--;
      y++;

      for (let j = startY + 1; j < endY && total > 0; j++) {
        result.push(matrix[y][x]);
        y++;
        total--;
      }
      
      for (let i = endX; i > startX && total > 0; i--) {
        result.push(matrix[y][x]);
        x--;
        total--;
      }

      for (let j = endY; j > startY && total > 0; j--) {
        result.push(matrix[y][x]);
        y--;
        total--;
      }
      x++;
      y++;
      startX++;
      endX--;
      startY++;
      endY--;
    }
    return result;
};