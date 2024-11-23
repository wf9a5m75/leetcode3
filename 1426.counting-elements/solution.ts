function countElements(arr: number[]): number {
  const freqOfElements = new Map<number, number>();
  // Counts up on each element
  for (const num of arr) {
      freqOfElements.set(num, freqOfElements.get(num) || 0 + 1);
  }
  
  // Counts up on arr[i] + 1 elements
  let result = 0;
  for (const num of arr) {
      if (!freqOfElements.has(num + 1)) {
          continue;
      }
      result += freqOfElements.get(num + 1)!;
  }
  return result;
};
