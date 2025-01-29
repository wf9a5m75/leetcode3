class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = [[]]
        for i in range(len(nums)):
            tmp = nums.pop(i)
            others = self.subsets(nums)

            n = len(results)
            for j in range(n):
                results.append(list(results[j]) + [tmp])

            nums.insert(i, tmp)

        return results
