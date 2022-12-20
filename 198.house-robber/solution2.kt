class Solution {
    fun rob(nums: IntArray): Int {
        val N = nums.size
        var mem = IntArray(3)

        for (i in N - 1 downTo 0) {
            val doNothing = mem[1]
            val doRobbering = mem[2] + nums[i]
            mem[0] = maxOf(doNothing, doRobbering)
            mem[2] = mem[1]
            mem[1] = mem[0]
        }
        return mem[0]
    }
}
