class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carryOver = 1
        for R in range(len(digits) - 1, -1, -1):
            s = digits[R] + carryOver
            digits[R] = s % 10
            carryOver = int(s / 10)
        if (carryOver == 0):
            return digits
        digits.insert(0, carryOver)
        return digits