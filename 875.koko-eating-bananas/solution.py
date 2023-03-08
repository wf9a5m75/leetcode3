class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEatAllBanana(h: int, k: int) -> bool:
            i = 0
            N = len(piles)
            hour = 0
            while (hour <= h) and (i < N):
                needHour = math.ceil(piles[i] / k)
                hour += needHour
                i += 1

            return (i == N) and (hour <= h)

        L = 1
        R = max(piles)
        while (L <= R):
            tmpK = (L + R) >> 1
            result = canEatAllBanana(h, tmpK)
            if (result):
                R = tmpK - 1
            else:
                L = tmpK + 1
        return L
