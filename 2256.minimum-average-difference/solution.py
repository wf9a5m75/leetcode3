class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        if (N == 1):
            return 0

        totalL = nums[0]
        totalR = sum(nums) - totalL

        cntL = 1
        cntR = N - 1
        minIdx = 0
        minDiff = abs(totalL - totalR // cntR)

        for i in range(1, N):
            cntL += 1
            cntR -= 1
            totalL += nums[i]
            totalR -= nums[i]

            if (cntR == 0):
                diff = abs(totalL//cntL)
            else:
                diff = abs(abs(totalL // cntL) - abs(totalR // cntR))
            # print(f"{totalL}//{cntL} - {totalR}//{cntR} = {diff}")

            if diff < minDiff:
                minDiff = diff
                minIdx = i
        return minIdx
