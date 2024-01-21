class Solution {
    public int rob(int[] nums) {
        int lengthOfNums = nums.length;
        if (lengthOfNums == 1) {
            return nums[0];
        }
        
        int[] dp = new int[lengthOfNums];
        
        dp[0] = nums[0];
        dp[1] = Math.max(dp[0], nums[1]);
        for (int i = 2; i < lengthOfNums; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
        }
        
        return dp[lengthOfNums - 1];
    }
}