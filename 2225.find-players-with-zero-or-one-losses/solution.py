class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = defaultdict(int)
        losses = defaultdict(int)
        players = set()
        for winner, loser in matches:
            wins[winner] += 1
            losses[loser] += 1
            players.add(winner)
            players.add(loser)
        
        notLostAnyMatches = []
        loseOnlyOnce = []
        for player in players:
            winCnt = wins[player]
            loseCnt = losses[player]
            if (winCnt > 0) and (loseCnt == 0):
                notLostAnyMatches.append(player)
                continue
            if (loseCnt == 1):
                loseOnlyOnce.append(player)
        return [
            sorted(notLostAnyMatches),
            sorted(loseOnlyOnce)
        ]