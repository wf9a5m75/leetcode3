import java.util.Stack

class Solution {
    fun calculate(val1: Int, action: String, val2: Int): String {
        return (when(action) {
            "+" -> val1 + val2
            "*" -> val1 * val2
            "-" -> val1 - val2
            "/" -> val1 / val2
            else -> "0"
        }).toString()
    }

    fun evalRPN(tokens: Array<String>): Int {
        val stack = Stack<String>()
        for (token in tokens) {
            stack.push(when(token) {
                "+", "-", "*", "/" -> {
                    val val2 = stack.pop().toInt()
                    val val1 = stack.pop().toInt()
                    this.calculate(val1, token, val2)
                }

                else -> token
            })
        }

        var result = 0
        for (token in stack) {
            result += token.toInt()
        }
        return result
    }
}
