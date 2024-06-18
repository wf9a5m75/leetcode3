class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        
        results = []
        start_time = intervals[0][0]
        end_time = intervals[0][1]
        for interval in intervals:
            if interval[0] <= end_time:
                end_time = max(end_time, interval[1])
                continue
                
            results.append([start_time, end_time])
            start_time = interval[0]
            end_time = interval[1]
        
        results.append([start_time, end_time])
        return results
        