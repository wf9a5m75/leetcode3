function maxSlidingWindow(nums: number[], k: number): number[] {
    let q: number[] = [];
    const results: number[] = [];
    const N = nums.length;
    for (let i = 0; i < N; i++) {
        while ((q.length > 0) && (i - q[0] >= k)) {
            q.shift();
        }
        while ((q.length > 0) && (nums[q.at(-1)!] <= nums[i])) {
            q.pop();
        }
        q.push(i);
        
        if (i < k - 1) {
            continue;
        }

        results.push(nums[q[0]]);
    }
    return results;
};