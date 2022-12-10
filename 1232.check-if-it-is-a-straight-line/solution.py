class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1 = coordinates[0][0], coordinates[0][1]
        x2,y2 = coordinates[1][0], coordinates[1][1]

        # https://hibikore-tanren.com/line-equation/
        def isOnStraight(x, y):
            return 0 == (y2 - y1) * (x - x1) - (x2 - x1) * (y - y1)

        return all(map(lambda coord: isOnStraight(coord[0], coord[1]), coordinates))
