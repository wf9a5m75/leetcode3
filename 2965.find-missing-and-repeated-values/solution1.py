class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        Flatten grid
        It's equivalent with

        nums = []
        for row in grid:
            for num in row:
                nums.append(num)
        """
        nums = [num for row in grid for num in row]
        n = len(nums)

        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)

        # Find the repeated number
        repeated = actual_sum - sum(set(nums))

        # Find the missing number
        missing = expected_sum - (actual_sum - repeated)

        return [repeated, missing]
