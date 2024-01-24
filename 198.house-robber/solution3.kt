class Solution {
    fun rob(nums: IntArray): Int {
        
        val N = nums.count()
        if (N == 1) {
            return nums[0]
        }
        val dp = Array<Int>(N){0}
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for (i in 2..N - 1) {
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        }
        
        // print(Arrays.toString(dp))
        return dp[N - 1]
    }
}