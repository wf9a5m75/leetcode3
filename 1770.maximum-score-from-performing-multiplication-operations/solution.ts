function maximumScore(nums: number[], multipliers: number[]): number {

  const cache = new Map<string, number>();
  
  const backtrack = (left: number, right: number, idx: number): number => {
      const key = `${left}_${right}`;
      if (cache.has(key)) {
          return cache.get(key)!;
      }
      if (left > right || idx === multipliers.length) {
          return 0;
      }
      
      const leftResult = backtrack(left + 1, right, idx + 1) + (nums[left] * multipliers[idx]);
      const rightResult = backtrack(left, right - 1, idx + 1) + (nums[right] * multipliers[idx]);
      const result = Math.max(leftResult, rightResult);
      cache.set(key, result);
      return result;
  }
  return backtrack(0, nums.length - 1, 0);
};
