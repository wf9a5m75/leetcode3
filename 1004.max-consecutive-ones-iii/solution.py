function longestOnes(nums: number[], k: number): number {
    const n = nums.length;
    let result = 0;
    let left = 0;
    let right = 0;
    let val = 0;
    
    // Counts up by each value: 0 and 1
    const counters = [0, 0];
    
    while(right < n) {
        // Moves the right pointer until number of 0 beyonds k
        while (right < n && counters[0] <= k) {
            val = nums[right];
            counters[val]++;
            right++;
        }
        
        // There are two cases:
        // - case1: number of 0 beyonds k, or
        // - case2: the right pointer byonds n.
        result = Math.max(result, right - left - (counters[0] === k + 1 ? 1 : 0));
        
        // Moves the left pointer until number of 0 meets k.
        while (left < right && counters[0] === k + 1) {
            val = nums[left];
            counters[val]--;
            left++;
        }
    }
    return result;
};
