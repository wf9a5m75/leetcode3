class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        totalLoad = sum(weights)
        maxLoad = max(weights)

        L = maxLoad
        R = totalLoad
        while (L < R):
            mid = (L + R) >> 1
            if (self.feasible(weights, mid, days)):
                R = mid
            else:
                L = mid + 1
        return L

    def feasible(self, weights: List[int], c: int, days: int) -> bool:
        daysNeeded = 1
        currentLoad = 0
        for weight in weights:
            currentLoad += weight
            if (currentLoad > c):
                currentLoad = weight
                daysNeeded += 1
        return daysNeeded <= days
