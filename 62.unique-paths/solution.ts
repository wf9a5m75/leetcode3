function uniquePaths(m: number, n: number): number {
  const matrix: number[][] = Array(m + 1);
  for (let i = 0; i < m + 1; i++) {
      matrix[i] = Array(n + 1).fill(0);
  }
  
  matrix[0][0] = 1;
  for (let y = 0; y < m; y++) {
      for (let x = 0; x < n; x++) {
          matrix[y + 1][x] += matrix[y][x];
          matrix[y][x + 1] += matrix[y][x];
      }
  }
  return matrix[m - 1][n - 1];
};
