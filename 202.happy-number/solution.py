class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while (n > 0) and (n not in seen):
            seen.add(n)

            nextN = 0
            while(n > 0):
                d = n % 10
                nextN += d ** 2
                n //= 10
            n = nextN

        return n == 1
