class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = list(range(n))
        counter = [0] * n
        for src, dst in trust:
            graph[src - 1] = dst - 1
            counter[dst - 1] += 1
        
        for i in range(n):
            if (graph[i] == i) and (counter[i] == n - 1):
                return (i + 1)
        return -1