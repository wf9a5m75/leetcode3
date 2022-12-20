/*
 * DP Top-Down:
 *   Time: O(N)
 *   Space: O(N)
 */
class Solution {
    fun rob(nums: IntArray): Int {
        val N = nums.size
        var mem = IntArray(N + 2)

        for (i in N - 1 downTo 0) {
            val doNothing = mem[i + 1]
            val doRobbering = mem[i + 2] + nums[i]
            mem[i] = maxOf(doNothing, doRobbering)
        }
        return mem[0]
    }
}
