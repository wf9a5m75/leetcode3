class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val mem = HashMap<Int, Int>()
        nums.forEachIndexed { i, num ->
            val rest = target - num
            if (mem.containsKey(rest)) {
                return intArrayOf(i, mem.get(rest)!!)
            }
            mem.put(num, i)
        }
        return intArrayOf(0, 0)
    }
}
