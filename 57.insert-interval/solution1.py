class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        results = []
        inserted = False
        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            if end < newInterval[0] or inserted:
                results.append([start, end])
                i += 1
                continue
            
            while i < len(intervals):
                start, end = intervals[i]
                if newInterval[1] < start:
                    results.append(newInterval)
                    inserted = True
                    break
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
                i += 1

        if inserted == False:
            results.append(newInterval)

        return results
        