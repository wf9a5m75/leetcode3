function minStartValue(nums: number[]): number {
  let prefixSum = 0;
  let smallestTotal = 0;
  for (const num of nums) {
      prefixSum += num;
      smallestTotal = Math.min(smallestTotal, prefixSum);
  }
  if (smallestTotal >= 0) {
      return 1;
  }
  return 1 - smallestTotal;
};
