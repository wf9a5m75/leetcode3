function triangleNumber(nums: number[]): number {
    // A triangle is established when the following all conditions:
    // (1) a + b > c
    // (2) b + c > a
    // (3) c + a > b

    // If the nums is sorted, we need to check only a + b > c
    //
    // e.g. nums = [2,2,3,4]
    // a + b = 2 + 2 > 3 ____ yes
    // a + b = 2 + 3 > 4 ____ yes
    // a + b = 2 + 3 > 4 ____ yes
    
    nums = nums.sort((a, b) => a - b);

    let result = 0;
    for (let i = 0; i < nums.length - 2; i++) {
        let k = i + 2;
        for (let j = i + 1; j < nums.length - 1 && nums[i] !== 0; j++) {
            while (k < nums.length && nums[i] + nums[j] > nums[k]) {
                k++;
            }
            result += k - j - 1;
        }
    }
    return result;
};
