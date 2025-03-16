class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.size = len(nums)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i in range(len(self.nums)):
            result += self.nums[i] * vec.at(i)
        return result
    
    def at(self, idx: int) -> int:
        if idx < 0 or idx >= self.size:
            return 0
        return self.nums[idx]
