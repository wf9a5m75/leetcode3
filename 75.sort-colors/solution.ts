/**
 Do not return anything, modify nums in-place instead.
 */
 function sortColors(nums: number[]): void {
    let zeroIdx = 0;
    let current = 0;
    let twoIdx = nums.length - 1;
    while (current <= twoIdx) {
        switch (nums[current]) {
            case 0: {
                [nums[current], nums[zeroIdx]] = [nums[zeroIdx], nums[current]];
                current++;
                zeroIdx++;
                break;
            }
            case 2: {
                [nums[current], nums[twoIdx]] = [nums[twoIdx], nums[current]];
                twoIdx--;
                break;
            }
            case 1: {
                current++;
                break;
            }
            default: {
                throw `unexpected value: ${nums[current]}`;
            }
        }
    }
};
