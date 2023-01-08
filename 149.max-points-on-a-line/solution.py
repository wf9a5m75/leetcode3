class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        N = len(points)
        if (N == 1):
            return 1

        # Since we can make at least one line,
        # result has at least two points
        result = 2
        for i in range(N):
            # We choose one point (points[i])
            # Then we try to calculate algles between all points except itself.
            #
            # If another points on a line, the tangent angle become the same.
            mem = {}
            for j in range(N):
                if i == j:
                    continue

                angle = math.atan2(points[j][1] - points[i][1],
                                   points[j][0] - points[i][0])

                mem[angle] = mem.get(angle, 0) + 1

            # +1 denotes the points[i] itself.
            result = max(result, max(mem.values()) + 1)
        return result
                
