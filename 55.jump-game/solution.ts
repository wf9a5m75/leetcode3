function canJump(nums: number[]): boolean {
  const dp = new Array(nums.length).fill(false);
  dp[0] = true;

  for (let i = 0; i < nums.length; i++) {
      if (!dp[i]) {
          continue;
      }
      for (let j = 1; j <= nums[i]; j++) {
          if (i + j >= nums.length) {
              return true;
          }
          dp[i + j] = true;
      }
  }
  return dp[nums.length - 1];
};