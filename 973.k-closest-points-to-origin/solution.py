class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceWithPoints = list(
            map(
                lambda point: [sqrt(pow(point[0], 2) + pow(point[1], 2)), point],
                points
            )
        )
        distanceWithPoints.sort()
        results = []
        for i in range(k):
            results.append(distanceWithPoints[i][1])
        return results