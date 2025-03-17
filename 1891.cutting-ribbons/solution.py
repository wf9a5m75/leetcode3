class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        total = 0
        largest = -inf
        for num in ribbons:
            total += num
            largest = max(largest, num)

        if k > total:
            return 0

        ribbons.sort(reverse = True)
        if k < len(ribbons):
            ribbons = ribbons[:k]
        
        L = 1
        R = largest
        while L <= R:
            mid = (L + R) >> 1
            numOfRibbons = self.tryToCut(ribbons, k, mid)
            if numOfRibbons < k:
                R = mid - 1
            else:
                L = mid + 1
        
        if self.tryToCut(ribbons, k, L) == 0:
            return R
        else:
            return L

    
    def tryToCut(self, ribbons: List[int], k: int, x: int) -> int:
        numOfRibbons = 0
        for num in ribbons:
            numOfRibbons += math.floor(num / x)
            if numOfRibbons >= k:
                return k
        return 0
