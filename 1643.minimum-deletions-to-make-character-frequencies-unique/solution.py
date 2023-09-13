class Solution:
    def minDeletions(self, s: str) -> int:
        
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        
        hq = []
        for char, cnt in counts.items():
            heapq.heappush(hq, -cnt)
        
        delete = 0
        while (len(hq) > 0):
            peakCnt = heapq.heappop(hq)
            while (len(hq) > 0) and (hq[0] == peakCnt):
                delete += 1
                cnt = heapq.heappop(hq)
                if (cnt + 1 == 0):
                    continue
                heapq.heappush(hq, cnt + 1)
        return delete