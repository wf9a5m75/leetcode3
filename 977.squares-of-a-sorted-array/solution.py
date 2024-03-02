class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Since the problem says that nums sorted in "non-decreasing order",
        # left side is lower than right side, at least.
        #
        # So, we can apply the two pointers approach.
        
        ans = [0] * 
        
        L = 0
        R = len(nums) - 1
        while (L <= R):
            absL = abs(nums[L])
            absR = abs(nums[R])
            if (absL >= absR):
                ans.append(absL * absL)
                L += 1
            else:
                ans.append(absR * absR)
                R -= 1
        ans.reverse()
        return ans