class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # nums = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,6,7,8]
        # k = 3
        # ans = [[1,1,1], [1,1,1],[2,2,2],[2,2,3],[3,3,3],[3,3,4],[4,4,4],[5,5,5],[6,7,8]]
        
        n = len(nums)
        if (n % 3 != 0):
            return []
        
        nums.sort()
        results = []
        
        i = 0
        while (i < n):
            j = i
            while (j < n) and (j < i + 3) and (nums[j] <= nums[i] + k):
                j += 1
            if (j - i != 3):
                return []
            results.append(nums[i:j])
            i = j
        
        return results
        
        