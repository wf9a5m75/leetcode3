class Solution {
    fun runningSum(nums: IntArray): IntArray {
        var prev = 0
        for (i in 0 .. nums.size - 1) {
            nums[i] += prev
            prev = nums[i]
        }
        return nums
    }
}
