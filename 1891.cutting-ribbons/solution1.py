class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        L = 0
        R = max(ribbons)
        while L < R:
            mid = (L + R + 1) // 2
            is_possible = self.tryToCut(ribbons, k, mid)
            if is_possible:
                L = mid
            else:
                R = mid - 1
        
        return L

    
    def tryToCut(self, ribbons: List[int], k: int, x: int) -> bool:
        numOfRibbons = 0
        for num in ribbons:
            numOfRibbons += math.floor(num / x)
            if numOfRibbons >= k:
                return True
        return False
