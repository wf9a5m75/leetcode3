class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        results = []
        
        # pop the first interval
        curr = intervals.pop(0)
        
        for start_time, end_time in intervals:
            if (start_time <= curr[1]):
                curr[1] = max(curr[1], end_time)
                continue
            
            results.append(curr)
            curr = [start_time, end_time]
        
        results.append(curr)
        return results