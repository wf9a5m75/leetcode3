function productExceptSelf(nums: number[]): number[] {
    
  const N = nums.length;
  let zeros = 0;
  
  let total = 1;
  for (let i = 0; i < N; i++) {
      if (nums[i] === 0) {
          zeros++;
          continue;
      }
      total *= nums[i];
  }
  
  switch (zeros) {
      case 0: {
          for (let i = 0; i < N; i++) {
              nums[i] = total / nums[i];
          }
          break;
      }
          
      case 1: {
          for (let i = 0; i < N; i++) {
              if (nums[i] === 0) {
                  nums[i] = total;
                  continue;
              }
              nums[i] = 0;
          }
          break;
      }
      
      default:
          for (let i = 0; i < N; i++) {
              nums[i] = 0;
          }
          break;
  }
  
  return nums;
};