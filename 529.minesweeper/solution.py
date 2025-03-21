class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        M, N = len(board), len(board[0])
        dp = [[0] * N for _ in range(M)]
        result = [[None] * N for _ in range(M)]

        for y in range(M):
            for x in range(N):
                if board[y][x] != "M":
                    continue
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        ny, nx = y + dy, x + dx
                        if ((dy == 0 and dx == 0) or 
                            (ny < 0 or ny == M or nx < 0 or nx == N)):
                            continue
                        dp[ny][nx] += 1

        clickY, clickX = click
        
        def dfs(y: int, x: int):
            if y < 0 or y == M or x < 0 or x == N:
                return

            if result[y][x] is not None:
                return

            if board[y][x] == "M":
                result[y][x] = "X"
                return
            
            if dp[y][x] == 0:
                # Prevent infinity recursion
                result[y][x] = "visiting"
                
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dy == 0 and dx == 0:
                            continue
                        dfs(y + dy, x + dx)
            
            result[y][x] = str(dp[y][x]) if dp[y][x] > 0 else "B"
        
        dfs(clickY, clickX)

        for y in range(M):
            for x in range(N):
                if result[y][x] is not None:
                    continue
                result[y][x] = board[y][x]

        return result
