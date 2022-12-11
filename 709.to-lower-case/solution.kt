import kotlin.math.*
class Solution {
    fun toLowerCase(s: String): String {
        val result = StringBuilder()
        for (c in s) {
            result.append(when {
                ('A' <= c) && (c <= 'Z') -> (c.toInt() or 32).toChar()
                else -> c
            })
        }
        return result.toString()
    }
}
