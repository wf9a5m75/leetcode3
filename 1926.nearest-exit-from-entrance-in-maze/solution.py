class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M, N = len(maze), len(maze[0])

        # Find the exit cells
        maze[ entrance[0] ][ entrance[1] ] = "Entrance"
        q = []
        for y in range(M):
            if (maze[y][0] == "."):
                q.append((y, 0))
                maze[y][0] = "+"

            if (maze[y][N - 1] == "."):
                q.append((y, N - 1))
                maze[y][N - 1] = "+"

        for x in range(N):
            if (maze[0][x] == "."):
                q.append((0, x))
                maze[0][x] = "+"

            if (maze[M - 1][x] == "."):
                q.append((M - 1, x))
                maze[M - 1][x] = "+"

        # If no exit, return -1
        if (len(q) == 0):
            return -1

        # Finding the shortest path from exits to the entrance (BFS)
        cnt = 1
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while(q):

            nextQ = []
            while(q):
                y,x = q.pop(0)

                for dy, dx in directions:
                    dy += y
                    dx += x
                    if (0 <= dy < M) and (0 <= dx < N):
                        if (maze[dy][dx] == "Entrance"):
                            return cnt
                        elif (maze[dy][dx] == "."):
                            nextQ.append((dy, dx))
                            maze[dy][dx] = "+"

            # If there is no next step, we can't move anymore.
            # Therefore, return -1
            if (len(nextQ) == 0):
                return -1
            cnt += 1
            q = nextQ
