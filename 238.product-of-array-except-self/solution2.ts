function productExceptSelf(nums: number[]): number[] {
  const results = new Array(nums.length).fill(0);

  let zeroCnt = 0;
  let allProduct = 1;
  for (const num of nums) {
      if (num === 0) {
          zeroCnt++;
          continue;
      }
      allProduct = allProduct * num;
  }
  
  if (zeroCnt > 1) {
      return results;
  }
  if (zeroCnt === 1) {
      for (let i = 0; i < nums.length; i++) {
          if (nums[i] !== 0) {
              continue;
          }
          results[i] = allProduct;
      }
  } else {
      for (let i = 0; i < nums.length; i++) {
          results[i] = allProduct / nums[i];
      }
  }
  return results;
};