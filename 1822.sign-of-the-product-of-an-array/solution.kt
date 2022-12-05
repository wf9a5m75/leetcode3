class Solution {
    fun arraySign(nums: IntArray): Int {
        var p = 1
        for (num in nums) {
            if (num == 0) {
                return 0
            } else if (num < 0) {
                p *= -1
            }
        }
        return p
    }
}
