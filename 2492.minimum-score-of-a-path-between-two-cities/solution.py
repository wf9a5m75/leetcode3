class UnionFind:
    def __init__(self, size: int):
        
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self, x: int) -> int:
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def connect(self, x: int, y: int):
        parentX = self.find(x)
        parentY = self.find(y)
        
        if (parentX == parentY):
            return
        
        elif (self.rank[parentX] < self.rank[parentY]):
            self.parent[parentX] = parentY
            
        elif (self.rank[parentX] > self.rank[parentY]):
            self.parent[parentY] = parentX
        
        else:
            self.parent[parentY] = parentX
            self.rank[parentX] += 1
        
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dsu = UnionFind(n + 1)
        result = float('inf')
        
        # Create a graph to connect all points
        for road in roads:
            dsu.connect(road[0], road[1])
        
        for road in roads:
            if (dsu.find(1) == dsu.find(road[0])):
                result = min(result, road[2])
        
        return result
