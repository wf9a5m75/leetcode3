class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if (source == destination):
            return True
        connected = {}
        for v1, v2 in edges:
            v1Dic = connected.get(v1, set())
            v1Dic.add(v2)
            connected[v1] = v1Dic

            v2Dic = connected.get(v2, set())
            v2Dic.add(v1)
            connected[v2] = v2Dic

        seen = [False] * n
        q = [source]
        while(q):
            curr = q.pop(0)
            if seen[curr]:
                continue

            seen[curr] = True
            for nextV in connected[curr]:
                if (seen[nextV]):
                    continue
                q.append(nextV)
                connected[nextV].remove(curr)

            connected[curr].clear()

        return seen[destination]
