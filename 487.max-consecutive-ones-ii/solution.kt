import kotlin.math.*
class Solution {
    fun findMaxConsecutiveOnes(nums: IntArray): Int {
        // Keeps the last 1 position
        var L = 0
        // Keeps the last 0 position
        var Z = 0
        // Denotes we have zero between L and R
        var hasZero = false

        // answer
        var result = 0

        for (R in 0..nums.size - 1) {
            if (nums[R] == 0) {
                if (hasZero) {
                    result = max(result, R - L)
                    L = Z + 1
                    Z = R
                } else {
                    Z = R
                    hasZero = true
                }
            }
        }

        result = max(result, nums.size - L)
        return result
    }
}
