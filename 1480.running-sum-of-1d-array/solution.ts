function runningSum(nums: number[]): number[] {
  let total = 0;
  return nums.map(num => {
      total += num;
      return total;
  });
};
