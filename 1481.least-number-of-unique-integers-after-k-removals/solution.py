class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        N = len(arr)
        if (N == k):
            return 0
        
        counts = Counter(arr)
        if k == 0:
            return len(counts.keys())
        
        # Integerを出現頻度でソートする
        uniqueNums = list(counts.keys())
        uniqueNums.sort(key = lambda k: counts[k])
        
        i = 0
        while (i < len(uniqueNums)):
            intNum = uniqueNums[i]
            if (k - counts[intNum] > 0):
                k -= counts[intNum]
                del counts[intNum]
                i += 1
                continue
                
            counts[intNum] = counts[intNum] - k
            if (counts[intNum] == 0):
                del counts[intNum]
            break
        
        return len(counts.keys())
        