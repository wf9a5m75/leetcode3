class Solution {
    fun findTheDifference(s: String, t: String): Char {
        var flag = 0
        val aInt = 'a'.toInt()

        for (i in 0 until s.length) {
            flag = flag xor (1 shl (s[i].toInt() - aInt))
        }
        for (i in 0 until t.length) {
            flag = flag xor (1 shl (t[i].toInt() - aInt))
        }

        var result = aInt
        while (flag != 1) {
            flag = flag shr 1
            result += 1
        }
        return result.toChar()
    }
}
