class Solution {
    fun canJump(nums: IntArray): Boolean {
        val N = nums.size
        if (N == 1) return true
        var i = 0
        var maxJmp = 0
        while ((i < N) && (i <= maxJmp) && (maxJmp < N)) {
            maxJmp = maxOf(maxJmp, i + nums[i])
            i++
        }
        return maxJmp >= N - 1
    }
}
