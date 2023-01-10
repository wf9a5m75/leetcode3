class NumArray(nums: IntArray) {
    val N = nums.size
    lateinit var dp: IntArray

    init {
        this.dp = IntArray(this.N)
        this.dp[0] = nums[0]
        for (i in 1..this.N - 1) {
            this.dp[i] = this.dp[i - 1] + nums[i]
        }
    }


    fun sumRange(left: Int, right: Int): Int {
        var total = 0
        if (left > 0) {
            total -= this.dp[left - 1]
        }
        return total + this.dp[right]
    }

}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */
