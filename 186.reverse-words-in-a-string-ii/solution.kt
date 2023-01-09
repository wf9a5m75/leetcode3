class Solution {
    fun reverseWords(s: CharArray): Unit {
        var L = 0
        var R = s.size - 1
        var tmp: Char = ' '
        val N = s.size

        // Flip the string overall
        while (L < R) {
            tmp = s[L]
            s[L] = s[R]
            s[R] = tmp
            L += 1
            R -= 1
        }

        // Flip each word
        L = 0
        R = 0
        while (R < N) {
            while ((R < N) && (s[R] != ' ')) R++

            val nextR = R + 1
            R -= 1
            while (L < R) {
                tmp = s[L]
                s[L] = s[R]
                s[R] = tmp
                L += 1
                R -= 1
            }
            L = nextR
            R = nextR
        }
    }
}
