class Solution {
    fun findWinners(matches: Array<IntArray>): List<List<Int>> {
        // TreeMap sorts keys automatically
        val losesMap = TreeMap<Int, Int>()
        
        for (match in matches) {
            val winner = match[0]
            val loser = match[1]
            
            losesMap[winner] = losesMap[winner] ?: 0
            losesMap[loser] = (losesMap[loser] ?: 0) + 1
        }
        
        val alwaysWinPlayers = ArrayList<Int>()
        val exactlyOnceLosers = ArrayList<Int>()
        for ((player, loseCnt) in losesMap) {
            if (loseCnt == 0) {
                alwaysWinPlayers.add(player)
                continue
            }
            if (loseCnt == 1) {
                exactlyOnceLosers.add(player)
            }
        }
        return listOf(
            alwaysWinPlayers.toList(),
            exactlyOnceLosers.toList(),
        )
    }
}