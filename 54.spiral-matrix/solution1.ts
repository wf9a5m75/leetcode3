function spiralOrder(matrix: number[][]): number[] {
    const m = matrix.length;
    const n = matrix[0].length;

    const result: number[] = [];
    let left = 0;
    let right = n - 1;
    let top = 0;
    let bottom = m - 1;
    while (left <= right && top <= bottom) {
        for (let i = left; i <= right; i++) {
            result.push(matrix[top][i]);
        }
        top++;

        for (let i = top; i <= bottom; i++) {
            result.push(matrix[i][right]);
        }
        right--;

        for (let i = right; i >= left && top <= bottom; i--) {
            result.push(matrix[bottom][i]);
        }
        bottom--;
        
        for (let i = bottom; i >= top && left <= right; i--) {
            result.push(matrix[i][left]);
        }
        left++;
    }

    return result;
};