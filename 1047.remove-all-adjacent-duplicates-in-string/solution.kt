class Solution {
    fun removeDuplicates(s: String): String {
        val stack = mutableListOf<Char>()
        for (c in s) {
            if ((stack.count() > 0) && (stack.last() == c)) {
                stack.removeAt(stack.count() - 1)
            } else {
                stack.add(c)
            }
        }
        return stack.joinToString("")
    }
}
