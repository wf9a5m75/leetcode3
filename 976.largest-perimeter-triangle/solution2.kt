class Solution {
    fun largestPerimeter(nums: IntArray): Int {
        nums.sortDescending()
        var A = nums[0]
        var B = nums[1]
        for (i in 2 until nums.size) {
            if ((A + B <= nums[i]) || (B + nums[i] <= A) || (A + nums[i] <= B)) {
                A = B
                B = nums[i]
                continue
            }
            return A + B + nums[i]
        }
        return 0

    }
}
