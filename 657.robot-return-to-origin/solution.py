class Solution:
    def judgeCircle(self, moves: str) -> bool:
        y = 0
        x = 0
        for move in moves:
            if (move == "L"):
                x -= 1
            elif (move == "R"):
                x += 1
            elif (move == "U"):
                y -= 1
            else:
                y += 1
        return (y == 0) and (x == 0)