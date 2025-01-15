class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        results = []
        n = len(nums)
        i = 0
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            if nums[i] > 0:
                break
            
            j = i + 1
            k = n - 1
            while j < k:
                calc = nums[i] + nums[j] + nums[k]
                if calc == 0:
                    results.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                    continue
                if calc < 0:
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return results