class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        results = []
        
        lastStart = -inf
        lastEnd = -inf
        for start, end in intervals:
            if lastEnd < start:
                results.append([start, end])
                lastStart = start
                lastEnd = end
                continue
            lastStart = min(lastStart, start)
            lastEnd = max(lastEnd, end)
            results.pop()
            results.append([lastStart, lastEnd])
        return results
