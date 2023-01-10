class Solution {
    fun largestPerimeter(nums: IntArray): Int {
        nums.sortDescending()
        val N = nums.size

        var A = nums[0]
        var B = nums[1]
        var C = 0
        for (i in 2..N - 1) {
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
