function topKFrequent(nums: number[], k: number): number[] {
    
  // Count up each number element
  const counts = new Map<number, number>();
  nums.forEach(num => counts.set(num, (counts.get(num) || 0) + 1));
  
  // Sort num elements based on the frequency
  const results: number[] = Array.from(counts.keys()).sort((a, b) => {
      return counts.get(b)! - counts.get(a)!;
  });
  
  results.length = k;
  return results;
};