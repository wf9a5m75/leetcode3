function rob(nums: number[]): number {
  if (nums.length === 1) {
      return nums[0];
  }

  let result = robbering(nums, 0, nums.length - 1);
  result = Math.max(result, robbering(nums, 1, nums.length));
  
  return result;
};

function robbering(nums: number[], start: number, end: number): number {
  const dp: number[] = new Array(nums.length + 2).fill(0);

  for (let i = start; i < end; i++) {
      // robbring
      dp[i + 2] = dp[i] + nums[i];
      // do nothing
      dp[i + 1] = Math.max(
          dp[i + 1],
          dp[i],
      );
  }
  // console.log(dp)
  return Math.max(dp[end], dp[end + 1]);
}