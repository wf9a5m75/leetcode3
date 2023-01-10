import java.util.Stack
class Solution {
    fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {
        var mem = HashMap<Int, Int>()
        var stack = Stack<Int>()

        for (val2 in nums2) {
            while ((stack.size > 0) && (stack.peek() < val2)) {
                mem[stack.pop()] = val2
            }
            mem[val2] = -1
            stack.push(val2)
        }

        var result = ArrayList<Int>()
        for (val1 in nums1) {
            result.add(mem[val1]!!)
        }
        return result.toIntArray()
    }
}
