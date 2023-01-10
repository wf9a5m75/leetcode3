class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        while(n > 0):
            d = n % 10
            s += d
            p *= d
            n //= 10
        return p - s
