class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = [0] * 100001
        losses = [0] * 100001
        for winner, loser in matches:
            wins[winner] += 1
            losses[loser] += 1
        
        notLostAnyMatches = []
        loseOnlyOnce = []
        for player in range(1, 100001):
            winCnt = wins[player]
            loseCnt = losses[player]
            if (winCnt > 0) and (loseCnt == 0):
                notLostAnyMatches.append(player)
                continue
            if (loseCnt == 1):
                loseOnlyOnce.append(player)
        return [
            notLostAnyMatches,
            loseOnlyOnce
        ]