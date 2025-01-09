function sortArrayByParity(nums: number[]): number[] {
    let evenIdx = 0;
    let oddIdx = nums.length - 1;
    let temp = 0;

    while (evenIdx < oddIdx) {
        if (nums[evenIdx] % 2 === 0) {
            evenIdx++;
            continue;
        }
        if (nums[oddIdx] % 2 === 1) {
            oddIdx--;
            continue;
        }

        temp = nums[evenIdx];
        nums[evenIdx] = nums[oddIdx];
        nums[oddIdx] = temp;
        evenIdx++;
        oddIdx--;
    }

    return nums;
};