class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = [False] * N
        visited[0] = True
        q = [newKey for newKey in rooms[0]]

        remainRooms = N - 1

        while (q):
            curr = q.pop(0)
            if (visited[curr]):
                continue
            visited[curr] = True
            remainRooms -= 1

            if (remainRooms == 0):
                break

            for newKey in rooms[curr]:
                if (visited[newKey]):
                    continue
                q.append(newKey)
        return remainRooms == 0
