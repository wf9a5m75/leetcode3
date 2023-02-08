class Solution {
    fun jump(nums: IntArray): Int {
        if (nums.size == 1) {
            return 0
        }

        var cnt = 0
        var nextMaxJmp = 0
        var maxJmp = 0
        for (i in 0 until nums.size) {
            if (nextMaxJmp < i + nums[i]) {
                nextMaxJmp = i + nums[i]
            }
            if (maxJmp == i) {
                maxJmp = nextMaxJmp
                cnt += 1
                if (maxJmp >= nums.size - 1) {
                    return cnt
                }
            }
        }
        return cnt
    }
}
