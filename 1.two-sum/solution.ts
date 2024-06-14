function twoSum(nums: number[], target: number): number[] {
  const memo = new Map<number, number>();
  
  for (let i = 0; i < nums.length; i++) {
      const num = nums[i];
      const rest = target - num;
      if (memo.has(rest)) {
          return [memo.get(rest)!, i];
      }
      memo.set(num, i);
  }
};