class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        nums.sort()
        for (i in 0 .. nums.size - 2) {
            if (nums[i] == nums[i + 1]) return true
        }
        return false
    }
}
