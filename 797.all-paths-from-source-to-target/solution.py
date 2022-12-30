class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = [[0]]
        results = []
        N = len(graph)
        while (q):
            nextQ = []
            for currPath in q:
                idx = currPath[-1]
                if (idx == N - 1):
                    results.append(currPath)
                    continue
                for nextV in graph[idx]:
                    nextQ.append(currPath + [nextV])
            q = nextQ
        return results
