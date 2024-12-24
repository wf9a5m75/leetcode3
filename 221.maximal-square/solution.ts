function maximalSquare(matrix: string[][]): number {
  const rows = matrix.length;
  const cols = matrix[0].length;
  
  const dp: number[][] = Array(rows + 1);
  for (let y = 0; y < rows + 1; y++) {
      dp[y] = Array(cols + 1).fill(0);
  }
  
  let maxSqlen = 0;
  for (let y = 1; y < rows + 1; y++) {
      for (let x = 1; x < cols + 1; x++) {
          if (matrix[y - 1][x - 1] === "0") {
              continue;
          }
          
          dp[y][x] = Math.min(
              dp[y][x - 1],
              dp[y - 1][x],
              dp[y - 1][x - 1],
          ) + 1;
          maxSqlen = Math.max(maxSqlen, dp[y][x]);
      }
  }
  return maxSqlen * maxSqlen;
};