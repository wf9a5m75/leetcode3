function getAverages(nums: number[], k: number): number[] {
  const results = Array(nums.length).fill(-1);
  const doubleK = k * 2;
  if (nums.length < doubleK + 1) {
      return results;
  }
  
  let partialSum = 0;
  for (let i = 0; i <= doubleK; i++) {
      partialSum += nums[i];
  }
  // Convert to 32 bit integer
  results[k] = ~~(partialSum / (doubleK + 1));
  
  for (let i = doubleK + 1; i < nums.length; i++) {
      partialSum = partialSum - nums[i - doubleK - 1] + nums[i];
      // Convert to 32 bit integer
      results[i - k] = ~~(partialSum / (doubleK + 1));
  }
  return results;
};
