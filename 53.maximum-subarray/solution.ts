function maxSubArray(nums: number[]): number {
  let currentSum = nums[0]; // Start with the first element
  let maxSum = nums[0];     // Start with the first element as max

  for (let i = 1; i < nums.length; i++) {
      // Either continue the current subarray or start a new one
      currentSum = Math.max(nums[i], currentSum + nums[i]);
      // Update maxSum if currentSum is larger
      maxSum = Math.max(maxSum, currentSum);
  }

  return maxSum;
};