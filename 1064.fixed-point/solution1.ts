export const solve = (nums: number[]): number => {
  let left = 0;
  let right = nums.length - 1;
  let answer = -1;
  while (left <= right) {
      const middle = Math.floor((left + right) / 2);
      switch (true) {
          case nums[middle] < middle:
              left = middle + 1;
              break;

          case nums[middle] === middle:
              answer = middle;
              right = middle - 1;
              break;

          case nums[middle] > middle:
              right = middle - 1;
              break;

          default:
              // Do nothing here.
              break;
      }
  }
  return answer;
};
