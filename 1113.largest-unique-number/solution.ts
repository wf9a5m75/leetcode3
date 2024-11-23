function largestUniqueNumber(nums: number[]): number {
  const possibilities = new Set<number>();
  const seen = new Set<number>();
  
  for (const num of nums) {
      if (seen.has(num)) {
          if (possibilities.has(num)) {
              possibilities.delete(num);
          }
          continue;
      }
      possibilities.add(num);
      seen.add(num);
  }
  if (possibilities.size === 0) {
      return - 1;
  }
  const finalists = Array.from(possibilities.values());
  finalists.sort((a, b) => b - a);
  return finalists[0];
};
