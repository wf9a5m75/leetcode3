class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        
        baskets = [0, 0]
        kinds = [0, -1]
        result = 0
        L = 0
        for R, fruit in enumerate(fruits):
            result = max(result, R - L)
            
            if (fruit == fruits[kinds[0]]):
                baskets[0] += 1
                #print(fruits[L:R + 1], baskets[0], baskets[1])
                continue
                
            if (kinds[1] == -1):
                baskets[1] = 1
                kinds[1] = R
                #print(fruits[L:R + 1], baskets[0], baskets[1])
                continue
                
            if (fruit == fruits[kinds[1]]):
                baskets[1] += 1
                #print(fruits[L:R + 1], baskets[0], baskets[1])
                continue
            
            while (baskets[0] > 0) and (baskets[1] > 0):
                if (fruits[kinds[0]] == fruits[L]):
                    baskets[0] -= 1
                else:
                    baskets[1] -= 1
                L += 1
            
            if (baskets[0] == 0):
                baskets[0] = 1
                kinds[0] = R
            else:
                baskets[1] = 1
                kinds[1] = R
            #print(fruits[L:R + 1], baskets[0], baskets[1])
            
        result = max(result, baskets[0] + baskets[1])
            
        return result