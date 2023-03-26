class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        dp = [0] * N

        maxCycle = -1
        serialCnt = 0
        for i in range(N):

            # already visited
            if (dp[i] > 0):
                continue

            startCnt = serialCnt
            idx = i
            cycleSize = -1
            while (idx != -1):

                # This edge has been visited before.
                if (dp[idx] > 0):

                    # Since serialCnt is increased always,
                    # dp[idx] > startCnt if we found this cycle in this turn.
                    # Otherwise, we visited here in previous turns.
                    if (dp[idx] > startCnt):
                        cycleSize = serialCnt - dp[idx] + 1
                    break
                else:
                    serialCnt += 1
                    dp[idx] = serialCnt
                    idx = edges[idx]

            maxCycle = max(maxCycle, cycleSize)
        return maxCycle
