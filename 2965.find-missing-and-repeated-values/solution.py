class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        results = [0, 0]
        counts = [0] * (n ** 2)
        for y in range(n):
            for x in range(n):
                counts[grid[y][x] - 1] += 1
        
        for i in range(n ** 2):
            if counts[i] == 2:
                results[0] = i + 1
            elif counts[i] == 0:
                results[1] = i + 1
        return results
