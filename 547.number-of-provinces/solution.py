class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        roots = [i for i in range(N)]
        ranks = [0] * N

        def find(x: int) -> int:
            parent = roots[x]
            if parent == x:
                return x
            roots[x] = find(parent)
            return roots[x]
        
        def union(a: int, b: int):
            a = find(a)
            b = find(b)
            if a == b:
                return
            rankA = ranks[a]
            rankB = ranks[b]
            if rankA < rankB:
                roots[b] = a
                ranks[b] += 1
            elif rankA > rankB:
                roots[a] = b
                ranks[a] += 1
            else:
                roots[b] = a
                ranks[b] += 1
        
        for i in range(N - 1):
            rootI = find(i)
            for j in range(i + 1, N):
                if isConnected[i][j] == 0:
                    continue
                union(rootI, j)
        
        numOfProvinces = 0
        for i in range(N):
            rootI = find(i)
            if i == rootI:
                numOfProvinces += 1
        return numOfProvinces
