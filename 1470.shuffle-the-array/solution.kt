class Solution {
    fun shuffle(nums: IntArray, n: Int): IntArray {
        val results = mutableListOf<Int>()
        for (i in 0..n-1) {
            results.add(nums[i])
            results.add(nums[n + i])
        }
        return results.toIntArray()
    }
}
