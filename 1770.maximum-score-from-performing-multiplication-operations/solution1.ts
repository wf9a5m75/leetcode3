function maximumScore(nums: number[], multipliers: number[]): number {

  let dpPast = Array<number>(multipliers.length + 1).fill(0);
  
  for (let i = multipliers.length - 1; i >= 0; i--) {
      const dpNext = Array<number>(multipliers.length + 1).fill(0);
      
      for (let j = i; j >= 0; j--) {
          const left = j;
          const right = nums.length - 1 - i + left;
          dpNext[j] = Math.max(
              nums[left] * multipliers[i] + dpPast[j + 1],
              
              nums[right] * multipliers[i] + dpPast[j],
          );
      }
      dpPast = dpNext;
  }
  return dpPast[0];
};