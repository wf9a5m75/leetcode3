class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        M, N = len(board), len(board[0])
        result = board[::]

        @cache
        def countMine(y: int, x: int) -> int:
            if board[y][x] == "M":
                return 1
            adjacents = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    ny, nx = y + dy, x + dx
                    if ((dy == 0 and dx == 0) or 
                        (ny < 0 or ny == M or nx < 0 or nx == N)):
                        continue
                    adjacents += 1 if board[ny][nx] == "M" else 0
            return adjacents

        clickY, clickX = click
        seen = set(["B", "1", "2", "3", "4", "5", "6", "7", "8", "9", "visiting"])
        
        def dfs(y: int, x: int):
            if y < 0 or y == M or x < 0 or x == N:
                return

            if result[y][x] in seen:
                return

            if board[y][x] == "M":
                result[y][x] = "X"
                return
            
            adjMines = countMine(y, x)
            if adjMines == 0:
                result[y][x] = "visiting"
                
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dy == 0 and dx == 0:
                            continue
                        dfs(y + dy, x + dx)
                result[y][x] = "B"
            else:
                result[y][x] = str(adjMines)
        
        dfs(clickY, clickX)

        return result
