class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        if n == 2 or n == 3:
            return []
        
        # Helper function that implements backtrack algorithm
        def backtrack(r: int):
            # Base case: if we've placed queens in all rows successfully
            if r == n:
                # Convert each row to string representation
                sol = ["".join(row) for row in board]
                ans.append(sol)
                return
            
            # Try placing queen in each column of current row
            for c in range(n):
                # Skip if column is attacked by another queen
                # - placedCol: same column
                # - placedPos: same positive diagonal (r + c)
                # - placedNeg: same negative diagonal (r - c)
                if (c in placedCol or
                    r + c in placedPos or 
                    r - c in placedNeg):
                    continue
                
                # Place queen and mark attacked position
                board[r][c] = "Q"
                placedCol.add(c)
                placedPos.add(r + c)
                placedNeg.add(r - c)

                # Recursively try to place queens in next rows
                backtrack(r + 1)

                # Backtrack: remove queen and unmark attacked positions
                board[r][c] = "."
                placedCol.remove(c)
                placedPos.remove(r + c)
                placedNeg.remove(r - c)
        
        # Intiialize empty chess board
        board = [["."] * n for _ in range(n)]

        # Sets to track attacked positions:
        placedCol = set() # Columns with queens
        placedPos = set() # Positive diagonals (r + c)
        placedNeg = set() # Negative diagonals (r - c)
        ans = [] # Stored all valid solutions

        # Start backtrack from row 0
        backtrack(0)
        return ans
