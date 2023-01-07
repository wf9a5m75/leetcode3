class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(cost)
        totalTank = 0
        currentTank = 0
        startingIdx = 0

        for i in range(N):
            afterMoving = gas[i] - cost[i]
            totalTank += afterMoving
            currentTank += afterMoving

            if (currentTank < 0):
                startingIdx = i + 1
                currentTank = 0

        return startingIdx if totalTank >= 0 else -1
