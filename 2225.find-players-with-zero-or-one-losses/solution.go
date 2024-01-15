func findWinners(matches [][]int) [][]int {
	n := len(matches)
	
	matchMap := make(map[int][2]int)
	for i := 0; i < n; i++ {
			match := matches[i]
			winner := match[0]
			loser := match[1]
			
			winnerStatsRecords := matchMap[winner]
			winnerStatsRecords[0]++
			matchMap[winner] = winnerStatsRecords
			
			loserStatsRecords := matchMap[loser]
			loserStatsRecords[1]++
			matchMap[loser] = loserStatsRecords
	}
	
	alwaysWinPlayers := make([]int, 0)
	loseExactlyOnePlayers := make([]int, 0)
	for player, stats := range matchMap {
			winCnt := stats[0]
			loseCnt := stats[1]
			
			if winCnt > 0 && loseCnt == 0 {
					alwaysWinPlayers = append(alwaysWinPlayers, player)
			} else if loseCnt == 1 {
					loseExactlyOnePlayers = append(loseExactlyOnePlayers, player)
			}
	}
	
	sort.Ints(alwaysWinPlayers)
	sort.Ints(loseExactlyOnePlayers)
	
	return [][]int{ alwaysWinPlayers, loseExactlyOnePlayers }
}