from typing import List

class Solution:
    board: List[List[str]]
    
    def initBoard(self):
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]
    
    def getGameResult(self) -> str:
        SIZE = 3
        
        diagnalLT_RB_A = 0
        diagnalLT_RB_B = 0
        
        diagnalRT_LB_A = 0
        diagnalRT_LB_B = 0
        
        filledCells = 0
        
        for i in range(SIZE):
            
            rowA = 0
            rowB = 0
            columnA = 0
            columnB = 0
            
            for j in range(SIZE):
                filledCells += 1 if self.board[i][j] else 0
                
                if (self.board[i][j] == "X"):
                    rowA += 1
                elif (self.board[i][j] == "O"):
                    rowB += 1
                
                if (self.board[j][i] == "X"):
                    columnA += 1
                elif (self.board[j][i] == "O"):
                    columnB += 1
                
            if (self.board[i][i] == "X"):
                diagnalLT_RB_A += 1
            elif (self.board[i][i] == "O"):
                diagnalLT_RB_B += 1
            
            k = SIZE - i - 1
            if (self.board[i][k] == "X"):
                diagnalRT_LB_A += 1
            elif (self.board[i][k] == "O"):
                diagnalRT_LB_B += 1
                
                
            if ((rowA == SIZE) or 
                (columnA == SIZE) or 
                (diagnalRT_LB_A == SIZE) or 
                (diagnalLT_RB_A == SIZE)):
                return "A"
            
            if ((rowB == SIZE) or 
                (columnB == SIZE) or 
                (diagnalRT_LB_B == SIZE) or 
                (diagnalLT_RB_B == SIZE)):
                return "B"
            
        return "Draw" if filledCells == SIZE * SIZE else "Pending"
    
    
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        self.initBoard()
        
        isTurnA = False
        for y, x in moves:
            isTurnA = not isTurnA
            player = "X" if isTurnA else "O"
            # Since the problem guarantees that the `moves` is valid.
            # So, we omit the empty checking of the cell.
            self.board[y][x] = player
        
        return self.getGameResult()