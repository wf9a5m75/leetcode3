function threeSum(nums: number[]): number[][] {
  let results: number[][] = [];
  nums.sort((a, b) => a- b);
  let target = 0;

  for (let i = 0; i < nums.length; i++) {
    if (i > 0 && nums[i - 1] === nums[i]) {
      continue;
    }
    if (nums[i] > target) {
      break;
    }

    let j = i + 1;
    let k = nums.length - 1;
    while (j < k) {
      const sum = nums[i] + nums[j] + nums[k];
      if (sum === target) {
        results.push([
          nums[i],
          nums[j],
          nums[k],
        ]);
        j++;
        k--;
        while (j < k && nums[j - 1] === nums[j]) {
          j++;
        }
        while (j < k && nums[k] === nums[k + 1]) {
          k--;
        }
      } else if (sum < target) {
        j++;
      } else {
        k--;
      }
    }
  }
  return results;
}