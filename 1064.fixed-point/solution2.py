from typing import List
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        L = 0
        R = len(arr) - 1
        ans = -1
        while (L <= R):
            mid = (L + R) >> 1
            if arr[mid] == mid:
                # update the answer
                ans = mid
                # We only need to check in the left side from the mid
                R = mid - 1
                continue
            
            if arr[mid] > mid:
                R = mid - 1
            else:
                L = mid + 1
        return ans
