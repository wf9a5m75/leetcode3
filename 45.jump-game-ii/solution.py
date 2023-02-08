class Solution:
    def jump(self, nums: List[int]) -> int:
        maxJmp = 0
        nextMaxJmp = 0

        N = len(nums)
        if (N == 1):
            return 0
        cnt = 0

        for i in range(N):

            if (nextMaxJmp < i + nums[i]):
                nextMaxJmp = i + nums[i]

            if (i == maxJmp):
                maxJmp = nextMaxJmp
                cnt += 1
                if (maxJmp >= N - 1):
                    return cnt
