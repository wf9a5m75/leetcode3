class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Sentinels
        intervals.insert(0, [-2, -1])
        intervals.append([100001, 100002])

        N = len(intervals)
        L = 0
        R = N - 1

        while (L <= R):
            mid = (L + R) >> 1
            if (intervals[mid][0] <= newInterval[0]):
                L = mid + 1
            else:
                R = mid - 1

        intervals.insert(L, newInterval)

        N += 1
        L -= 1
        while (L + 1 < N):
            while (L + 1 < N) and (intervals[L][1] >= intervals[L + 1][0]):
                intervals[L][0] = min(intervals[L][0], intervals[L + 1][0])
                intervals[L][1] = max(intervals[L][1], intervals[L + 1][1])
                intervals.pop(L + 1)
                N -= 1
            L += 1

        intervals.pop(0)
        intervals.pop()

        return intervals
