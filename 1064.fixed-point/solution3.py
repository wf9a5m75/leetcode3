from typing import List
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        answer = -1
        while left <= right:
            middle = int((left + right) / 2)
            
            if arr[middle] < middle:
                left = middle + 1
            elif arr[middle] == middle:
                answer = middle
                right = middle - 1
            else:
                right = middle - 1
        return answer
