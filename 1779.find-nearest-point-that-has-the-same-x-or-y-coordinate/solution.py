class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        nearestDistance = float('inf')
        nearestIdx = -1

        for i, point in enumerate(points):
            if (point[0] != x) and (point[1] != y):
                continue

            distance = sqrt(abs(point[0] - x) ** 2
                            + abs(point[1] - y) ** 2)

            if (nearestDistance <= distance):
                continue

            nearestDistance = distance
            nearestIdx = i

        return nearestIdx
            
