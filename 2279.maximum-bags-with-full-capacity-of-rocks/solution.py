class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        hq = []
        N = len(capacity)
        for i in range(N):
            heapq.heappush(hq, capacity[i] - rocks[i])

        cnt = 0
        while (additionalRocks > 0) and (len(hq) > 0):
            peek = heapq.heappop(hq)
            if (additionalRocks >= peek):
                cnt += 1
            additionalRocks -= peek

        return cnt
