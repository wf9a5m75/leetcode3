from typing import List

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        return self.binarySearchWithBounds(arr, 0, len(arr) - 1)
        
    def binarySearchWithBounds(self, arr: List[int], start: int, end: int) -> int:
        if (start > end):
            return -1
        L = start
        R = end
        while L <= R:
            mid = (L + R) >> 1
            if arr[mid] == mid:
                left_side = self.binarySearchWithBounds(arr, L, mid - 1)
                if left_side > -1:
                    return left_side
                return mid
            
            if arr[mid] < mid:
                L = mid + 1
            else:
                R = mid - 1
        return -1
