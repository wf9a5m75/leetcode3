class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        M, N = len(board), len(board[0])
        battleShips = 0
        for y in range(M):
            for x in range(N):
                if (board[y][x] == "."):
                    continue
                
                if (y - 1 >= 0 and
                    board[y - 1][x] == "X"):
                    continue
                if (x - 1 >= 0 and
                    board[y][x - 1] == "X"):
                    continue

                battleShips += 1
        return battleShips
