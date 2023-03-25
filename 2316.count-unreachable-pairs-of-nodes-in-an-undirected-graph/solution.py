class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parent = [i for i in range(n)]
        self.counts = [0] * n

    def findParent(self, x: int) -> int:
        if (self.parent[x] != x):
            self.parent[x] = self.findParent(self.parent[x])
        return self.parent[x]

    def union(self, A: int, B: int):

        A = self.findParent(A)
        B = self.findParent(B)
        if (A == B):
            return
        elif (self.counts[A] < self.counts[B]):
            self.parent[A] = B
        elif (self.counts[A] > self.counts[B]):
            self.parent[B] = A
        else:
            self.parent[B] = A
            self.counts[A] += 1

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        dsu = UnionFind(n)

        for A, B in edges:
            dsu.union(A, B)

        groups = defaultdict(int)
        for i in range(n):
            parent = dsu.findParent(i)
            groups[parent] += 1


        numOfPaths = 0
        remainNodes = n
        for grpCnt in groups.values():
            numOfPaths += grpCnt * (remainNodes - grpCnt)
            remainNodes -= grpCnt

        return numOfPaths

        
