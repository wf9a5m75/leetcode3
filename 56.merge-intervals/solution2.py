class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort by start_time, end_time
        intervals.sort()
        
        # pop the first interval
        results = [intervals.pop(0)]
        
        # traverse from the second interval
        for start_time, end_time in intervals:
            
            # If the interval starts before the previous end time,
            # merge them.
            if (start_time <= results[-1][1]):
                results[-1][1] = max(results[-1][1], end_time)
                continue
            
            # New interval
            results.append([start_time, end_time])
        return results