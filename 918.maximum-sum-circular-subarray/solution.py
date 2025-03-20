from collections import deque
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n * 2 + 1)
        for i in range(n * 2):
            prefixSum[i + 1] = prefixSum[i] + nums[i % n]
        
        # For given i, find max prefixSum[i] - prefixSum[j]
        # Given contraint j - i <= n.
        #
        # Montonic increasing queue
        dq = deque()
        result = -inf
        for i in range(n * 2):
            while dq and i - dq[0] > n:
                dq.popleft()

            if dq:
                result = max(result, prefixSum[i] - prefixSum[dq[0]])
            
            while dq and prefixSum[dq[-1]] >= prefixSum[i]:
                dq.pop()
            
            dq.append(i)
        return result
