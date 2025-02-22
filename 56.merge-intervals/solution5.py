class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = list(sorted(intervals))
        
        merged = []
        prev = [-inf, -inf]
        for start, end in sorted_intervals:
            if (prev[0] <= start <= prev[1] or 
                start <= prev[1] <= end):
                prev[1] = max(prev[1], end)
            else:
                merged.append(prev)
                prev = [start, end]
        merged.append(prev)
        merged.pop(0)
        return merged
