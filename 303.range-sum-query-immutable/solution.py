class NumArray:

    def __init__(self, nums: List[int]):
        self.N = len(nums)
        self.dp = [0] * self.N

        self.dp[0] = nums[0]
        for i in range(1, self.N):
            self.dp[i] = self.dp[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        if (left > 0):
            total -= self.dp[left - 1]
        total += self.dp[right]
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
