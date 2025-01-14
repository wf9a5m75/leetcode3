class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        cols = len(mat[0])
        rows = len(mat)
        results = [[inf] * cols for _ in range(rows)]

        for y in range(rows):
            for x in range(cols):
                if mat[y][x] == 0:
                    results[y][x] = 0
                if y + 1 < rows:
                    results[y + 1][x] = min(results[y + 1][x], results[y][x] + 1)
                if x + 1 < cols:
                    results[y][x + 1] = min(results[y][x + 1], results[y][x] + 1)
                
        for y in range(rows - 1, -1, -1):
            for x in range(cols - 1, -1, -1):
                if mat[y][x] == 0:
                    results[y][x] = 0
                if y - 1 >= 0:
                    results[y - 1][x] = min(results[y - 1][x], results[y][x] + 1)
                if x - 1 >= 0:
                    results[y][x - 1] = min(results[y][x - 1], results[y][x] + 1)
        return results
    