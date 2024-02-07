class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0:
            return []
        
        results = set()
        if x == 1:
            maxX = 2
        else:
            maxX = int(math.log10(bound) / math.log10(x)) + 1
        if y == 1:
            maxY = 2
        else:
            maxY = int(math.log10(bound) / math.log10(y)) + 1
        
        for i in range(maxX):
            for j in range(maxY):
                tmp = x ** i + y ** j
                if (tmp > bound):
                    continue
                results.add(tmp)
        return results