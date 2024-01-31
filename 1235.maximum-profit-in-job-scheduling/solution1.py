class Schedule:
    def __init__(self, start:int, end: int, profit: int):
        self.start = start
        self.end = end
        self.profit = profit
        
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        
        schedules = [Schedule(
            startTime[i],
            endTime[i],
            profit[i]
        ) for i in range(N)]
        
        schedules.sort(key=lambda x: x.start)
        
        def getNextSchedule(target: int) -> int:
            L = 0
            R = N - 1
            while (L <= R):
                mid = (L + R) >> 1
                if (schedules[mid].start < target):
                    L = mid + 1
                else:
                    R = mid - 1
            return L
        
        dp = [0] * (N + 1)
        for i in range(N):
            # do nothing
            dp[i + 1] = max(dp[i + 1], dp[i])
            
            # do something
            schedule = schedules[i]
            nextTaskIdx = getNextSchedule(schedule.end)
            dp[nextTaskIdx] = dp[i] + schedule.profit
        return dp[N]
        
#         @cache
#         def backtrack(i: int) -> int:
#             if (i == N):
#                 return 0
            
#             doNothing = backtrack(i + 1)
            
#             schedule = schedules[i]
#             nextTaskIdx = getNextSchedule(schedule.end)
#             doSomething = backtrack(nextTaskIdx) + schedule.profit
            
#             return max(doNothing, doSomething)
        
#         return backtrack(0)