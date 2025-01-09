function runningSum(nums: number[]): number[] {
  let prefix = 0;
  return nums.map(num => {
      prefix = prefix + num;
      return prefix;
  });
};