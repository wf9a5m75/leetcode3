class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while(L <= R):
            mid = (L + R) >> 1
            if (nums[mid] <= target):
                L = mid + 1
            else:
                R = mid - 1
        if nums[R] == target:
            return R
        else:
            return L
