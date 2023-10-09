class Solution:
    def binarySearch1(self, nums: List[int], target: int, L: int, R: int) -> int:
        while (L <= R):
            mid = (L + R) >> 1
            if (nums[mid] >= target):
                R = mid - 1
            else:
                L = mid + 1
        return L
    def binarySearch2(self, nums: List[int], target: int, L: int, R: int) -> int:
        while (L <= R):
            mid = (L + R) >> 1
            if (nums[mid] <= target):
                L = mid + 1
            else:
                R = mid - 1
        return L
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        if (N == 0):
            return [-1, -1]
        if (N == 1):
            if (nums[0] == target):
                return [0, 0]
            else:
                return [-1, -1]
        
        L = self.binarySearch1(nums, target, 0, N - 1)
        if (L == -1) or (L == N) or (nums[L] != target):
            return [-1, -1]
        
        
        R = self.binarySearch2(nums, target, L, N - 1)
        return [L, R - 1]