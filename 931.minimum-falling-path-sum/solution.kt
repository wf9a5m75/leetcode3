import kotlin.math.min

class Solution {
    fun minFallingPathSum(matrix: Array<IntArray>): Int {
        val m = matrix.size
        val n = matrix[0].size
        
        val MAX_INT = (2.toDouble().pow(31) - 1).toInt()
        val dp = Array(2, { Array(n, { 0 }) })
        var result = MAX_INT
        
        var srcIdx = 0
        var dstIdx = 1
        for (y in 0 .. m - 1) {
            for (x in 0 .. n - 1) {
                dp[dstIdx][x] = MAX_INT
            }
            
            for (x in 0 .. n - 1) {
                if (x > 0) {
                    dp[dstIdx][x - 1] = min(dp[dstIdx][x - 1], dp[srcIdx][x] + matrix[y][x])
                }
                
                dp[dstIdx][x] = min(dp[dstIdx][x], dp[srcIdx][x] + matrix[y][x])
                
                if (x + 1 < m) {
                    dp[dstIdx][x + 1] = min(dp[dstIdx][x + 1], dp[srcIdx][x] + matrix[y][x])
                }
            }
            srcIdx = (srcIdx + 1) % 2
            dstIdx = (dstIdx + 1) % 2
        }
        
        for (x in 0 .. n - 1) {
            result = min(result, dp[srcIdx][x])
        }
        return result
    }
}