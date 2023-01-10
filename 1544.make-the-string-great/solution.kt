class Solution {
    fun makeGood(s: String): String {
        val stack = Stack<Char>()
        for (char in s) {
            if (stack.size > 0) {
                val isLower = char.isLowerCase()
                val lastChar = stack.peek()
                val isLastLower = lastChar.isLowerCase()

                val lwChar = char.toLowerCase()
                val upChar = char.toUpperCase()

                if ((isLastLower && !isLower && lwChar == lastChar) ||
                    (!isLastLower && isLower && upChar == lastChar)) {
                    stack.pop()
                    continue
                }
            }
            stack.push(char)
        }
        var result = ""
        while (stack.size > 0) {
            result = "${stack.pop()}${result}"
        }
        return result
    }
}
