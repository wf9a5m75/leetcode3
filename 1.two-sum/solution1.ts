function twoSum(nums: number[], target: number): number[] {
  const indiciesByNumber = new Map<number, number>();
  for (let i = 0; i < nums.length; i++) {
      const rest = target - nums[i];
      if (indiciesByNumber.has(rest)) {
          // We found the pairs
          return [i, indiciesByNumber.get(rest)!];
      }
      indiciesByNumber.set(nums[i], i);
  }
};