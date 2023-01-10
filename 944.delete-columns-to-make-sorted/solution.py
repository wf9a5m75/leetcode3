class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        M, N = len(strs), len(strs[0])
        result = 0
        for x in range(N):
            prev = -1
            for y in range(M):
                cOrder = ord(strs[y][x])
                if prev <= cOrder:
                    prev = cOrder
                    continue
                result += 1
                break
        return result
