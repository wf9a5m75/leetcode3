class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        
        int val = 0;
        
        int srcIdx = 0;
        int dstIdx = 1;
        int MAX_INT = (int)((long)Math.pow(2, 31) - 1);
        int result = MAX_INT;
        
        int[][] dp = new int[2][];
        dp[0] = new int[m];
        dp[1] = new int[m];
        
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                dp[dstIdx][x] = MAX_INT;
            }
            for (int x = 0; x < m; x++) {
                val = matrix[y][x];
                
                if (x > 0) {
                    dp[dstIdx][x - 1] = Math.min(dp[dstIdx][x - 1], dp[srcIdx][x] + val);
                }
                dp[dstIdx][x] = Math.min(dp[dstIdx][x], dp[srcIdx][x] + val);
                
                if (x + 1 < m) {
                    dp[dstIdx][x + 1] = Math.min(dp[dstIdx][x + 1], dp[srcIdx][x] + val);
                }
            }
            srcIdx = (srcIdx + 1) % 2;
            dstIdx = (dstIdx + 1) % 2;
        }
        
        for (int x = 0; x < m; x++) {
            result = Math.min(result, dp[srcIdx][x]);
        }
        
        return result;
    }
}