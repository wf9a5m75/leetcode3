function trap(height: number[]): number {
  const stack: number[] = [];
  let result = 0;
  let i = 0;
  while (i < height.length) {
      while (stack.length > 0 && height[stack.at(-1)!] < height[i]) {
          const poped = stack.pop()!;
          if (stack.length === 0) {
              break;
          }
          const distance = i - stack.at(-1)! - 1;
          const shorter = Math.min(height[stack.at(-1)!] , height[i]);
          result += (shorter - height[poped]) * distance;
      }
      stack.push(i);
      i++;
  }
  return result;
};