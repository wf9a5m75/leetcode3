import kotlin.math.*
class Solution {
    fun mergeAlternately(word1: String, word2: String): String {
        var i = 0
        val len1 = word1.length
        val len2 = word2.length
        var limit = min(len1, len2)

        var result = ""
        while (i < limit) {
            result += "${word1[i]}${word2[i]}"
            i++
        }

        limit = max(len1, len2)
        when {
            i < len1 -> return result + word1.substring(i)
            i < len2 -> return result + word2.substring(i)
            else -> return result
        }

    }
}
