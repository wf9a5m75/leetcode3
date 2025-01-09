function removeElement(nums: number[], val: number): number {
    let writeIdx = 0;
    for (let readIdx = 0; readIdx < nums.length; readIdx++) {
        if (nums[readIdx] === val) {
            continue;
        }
        nums[writeIdx] = nums[readIdx];
        writeIdx++;
    }
    return writeIdx;
};