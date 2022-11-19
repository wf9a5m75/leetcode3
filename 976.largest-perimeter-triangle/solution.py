class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)

        N = len(nums)
        A, B = nums[0], nums[1]
        for i in range(2, N):
            C = nums[i]

            if (A + B > C) and (B + C > A) and (A + C > B):
                return A + B + C
            A, B = B, C
        return 0
