class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        INF = float('inf')
        result = INF
        resultIdx = -1
        for i, point in enumerate(points):
            dx = point[0] - x
            dy = point[1] - y
            if (dx != 0) and (dy != 0):
                continue
            distance = abs(dx) + abs(dy)
            if distance < result:
                result = distance
                resultIdx = i
        return resultIdx
