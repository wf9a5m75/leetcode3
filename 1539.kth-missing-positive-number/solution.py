class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnt = 0
        j = 0
        exp = 1
        N = len(arr)
        i = 0
        while (i <= arr[-1]) and (j < N):
            if (exp != arr[j]):
                cnt += 1
                if (cnt == k):
                    return exp
            else:
                j += 1
            exp += 1
        return exp + (k - cnt) - 1
            
