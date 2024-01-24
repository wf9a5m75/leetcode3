class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        int[] results = new int[] {0, 0};
        int expectSum = (n * (n + 1)) >> 1;
        int sumOfNums = 0;
        
        for (int i = 0; i < n; i++) {
            int val = Math.abs(nums[i]);
            sumOfNums += val;
            
            if (nums[val - 1] < 0) {
                results[0] = val;
            }
            nums[val - 1] *= -1;
        }
        results[1] = results[0] + expectSum - sumOfNums;
        return results;
    }
}