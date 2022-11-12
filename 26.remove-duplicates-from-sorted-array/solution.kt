class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        var ptrW = 0
        var prev = -10000
        nums.forEachIndexed {
            idx, num ->
                if (prev != num) {
                    prev = num
                    nums[ptrW] = num
                    ptrW += 1
                }
        }
        return ptrW
    }
}
