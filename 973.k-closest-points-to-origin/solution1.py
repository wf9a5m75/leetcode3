from heapq import heappush,heappushpop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for i in range(len(points)):
            x, y = points[i]
            distance = sqrt(pow(x, 2) + pow(y, 2))
            if i < k:
                heappush(q, [-distance, [x, y]])
            else:
                heappushpop(q, [-distance, [x, y]])
        
        results = list(map(lambda x: x[1], q))
        return results
