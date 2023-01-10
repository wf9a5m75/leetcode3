class Solution {
    fun moveZeroes(nums: IntArray): Unit {
        var pwrite = 0
        var pread = 0
        val N = nums.size

        while(pread < N) {
            if (nums[pread] != 0) {
                nums[pwrite++] = nums[pread]
            }
            pread += 1
        }
        while(pwrite < N) nums[pwrite++] = 0
    }
}
