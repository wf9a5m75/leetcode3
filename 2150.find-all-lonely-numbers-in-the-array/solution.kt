class Solution {
    fun findLonely(nums: IntArray): List<Int> {
        val N = nums.size
        if (N == 1)
            return listOf<Int>(nums[0])

        nums.sort()
        val results = ArrayList<Int>()
        var prev = true
        var current = (nums[0] + 1 < nums[1])

        nums.forEachIndexed { i, num ->
            current = (i == N - 1) || (nums[i] + 1 < nums[i + 1])
            if (prev && current) {
                results.add(num)
            }
            prev = current
        }
        return results.toList<Int>()
    }
}
