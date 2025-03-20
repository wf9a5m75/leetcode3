"""
The n depict the number of elements in the nums variable.

TC: O(n log k)
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        n = len(nums)
        window = []

        def insert(target: int):
            L = 0
            R = len(window) - 1
            while L <= R:
                mid = (L + R) >> 1
                if window[mid] < target:
                    L = mid + 1
                else:
                    R = mid - 1
            window.insert(L, target)
        
        def remove(target: int):
            L = 0
            R = len(window) - 1
            while L <= R:
                mid = (L + R) >> 1
                if window[mid] < target:
                    L = mid + 1
                else:
                    R = mid - 1
            window.pop(L)


        for i, num in enumerate(nums):
            if i - k >= 0:
                remove(nums[i - k])

            insert(num)

            if i - k + 1 >= 0:
                results.append(window[-1])
                
        return results
