class Solution:
    def isUgly(self, n: int) -> bool:
        if (n < 2):
            return (n == 1)

        def keepDividing(n, divisor):
            while (n % divisor == 0):
                n //= divisor
            return n

        # Remove 2,3, and 5 primary factors
        for factor in [2, 3, 5]:
            n = keepDividing(n, factor)

        # Since n does not have 2,3,5 factors, n should be 1
        # Otherwise, n still contains other factors.
        return n == 1
