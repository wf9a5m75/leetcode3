class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        p1 = 0
        p2 = n
        N2 = len(nums)
        results = []
        while (p2 < N2):
            results.append(nums[p1])
            results.append(nums[p2])
            p1 += 1
            p2 += 1
        return results
