/*
 * Backtracking:
 *   Time: O(N)
 *   Space: O(N)
 */
class Solution {
    fun rob(nums: IntArray): Int {
        val N = nums.size
        var mem = IntArray(N)
        mem.fill(-1)

        fun backtrack(i: Int): Int {
            if (i >= N) return 0
            if (mem[i] >= 0) return mem[i]

            val doNothing = backtrack(i + 1)
            val doRobbering = backtrack(i + 2) + nums[i]
            mem[i] = maxOf(doNothing, doRobbering)
            return mem[i]
        }
        return backtrack(0)
    }
}
