class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        N = len(nums)

        for num in nums:
            while (stack) and (stack[-1] > num):
                stack.pop()
            stack.append(num)

        while (len(stack) > k):
            stack.pop()
        return stack
