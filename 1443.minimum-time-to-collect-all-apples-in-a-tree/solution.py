class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        result: int = 0

        parents = [-1] * n
        seen = [False] * n
        seen[0] = True

        for a, b in edges:
            if seen[a] == True:
                parents[b] = a
            else:
                parents[a] = b

            seen[b] = True

        visited = [False] * n
        visited[0] = True

        for parent in range(1, n):
            if hasApple[parent] == False:
                continue
            result += 1
            visited[parent] = True

            # climb up to root until we already visited vertix
            parent = parents[parent]
            while not visited[parent]:
                result += 1
                visited[parent] = True
                parent = parents[parent]
        return 2 * result
