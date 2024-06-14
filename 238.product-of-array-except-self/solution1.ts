function productExceptSelf(nums: number[]): number[] {
    
  const N = nums.length;
  const results: number[] = Array(N).fill(1);
  let prefix = 1;
  let suffix = 1;
  
  for (let i = 0; i < N; i++) {
      results[i] *= prefix;
      results[N - i - 1] *= suffix;
      prefix *= nums[i];
      suffix *= nums[N - i - 1];
  }
  return results;
};