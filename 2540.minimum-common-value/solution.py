from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = p2 = 0
        N, M = len(nums1), len(nums2)
        while (p1 < N) and (p2 < M) and (nums1[p1] != nums2[p2]):
            if (nums1[p1] < nums2[p2]):
                p1 = self.nextIdx(nums1, p1 + 1, N - 1, nums2[p2])
            else:
                p2 = self.nextIdx(nums2, p2 + 1, M - 1, nums1[p1])
        
        if (p1 < N) and (p2 < M) and (nums1[p1] == nums2[p2]):
            return nums1[p1]
        return -1
    
    def nextIdx(self, nums: List[int], L: int, R: int, target: int) -> int:
        while (L <= R):
            mid = (L + R) >> 1
            if (nums[mid] < target):
                L = mid + 1
            else:
                R = mid - 1
        return L