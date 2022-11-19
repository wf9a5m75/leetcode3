class Solution {
    fun largestPerimeter(nums: IntArray): Int {
        nums.sort()
        var N = nums.size
        var A = nums[N - 1]
        var B = nums[N - 2]
        var C = 0

        for (i in nums.size - 3 downTo 0) {
            C = nums[i]
            if ((A + B > C) && (B + C > A) && (A + C > B)) {
                return A + B + C
            }
            A = B
            B = C
        }

        return 0
    }
}
