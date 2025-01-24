function permute(nums: number[]): number[][] {
    const n = nums.length;
    if (n === 1) {
        return [[nums[0]]];
    }

    const results: number[][] = [];
    for (let i = 0; i < n; i++) {
        const tmp = nums.splice(i, 1).pop()!;
        const another = permute(nums);

        for (const other of another) {
            other.splice(0, 0, tmp);
            results.push(other);
        }
        nums.splice(i, 0, tmp);
    }
    return results;
};