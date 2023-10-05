class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        threathold = len(nums) / 3
        results = []
        for num in counts.keys():
            if (counts[num] <= threathold):
                continue
            results.append(num)
        return results