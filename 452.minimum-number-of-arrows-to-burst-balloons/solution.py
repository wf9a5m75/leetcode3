class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by the end points
        points.sort(key = lambda point: point[1])

        N = len(points)

        result = 0
        i = 0

        # The end point of the first points has to be included for one shot.
        # Thus maxX is the points[0][1]
        # If there is another points before maxX, we can shot them togher..
        maxX = points[0][1]
        while (i < N):
            while (i < N) and (points[i][0] <= maxX):
                i += 1
            result += 1
            if (i < N):
                maxX = points[i][1]
        return result
