import java.util.Stack
class Solution {
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        val stack = Stack<Int>()
        var answer = IntArray(temperatures.size)

        for ((i, temp) in temperatures.withIndex()) {
            while (!stack.empty() && (temperatures[stack.peek()] < temp)) {
                val idx = stack.pop()
                answer[idx] = i - idx
            }
            stack.push(i)
        }
        return answer
    }
}
