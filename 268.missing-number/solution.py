function missingNumber(nums: number[]): number {
    const n = nums.length;
    let xorSum = 0;
    for (let i = 1; i <= n; i++) {
        xorSum = xorSum ^ i;
    }
    for (const num of nums) {
        xorSum = xorSum ^ num;
    }
    return xorSum;
};
