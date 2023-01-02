class Solution {
    fun detectCapitalUse(word: String): Boolean {
        val ALL_UPPER = word.toUpperCase()
        val ALL_LOWER = word.toLowerCase()
        val FIRST_UPPER = "${ALL_UPPER[0]}${ALL_LOWER.substring(1)}"

        // println("${word} ${ALL_UPPER} ${ALL_LOWER} ${FIRST_UPPER}")

        return (ALL_UPPER == word) || (ALL_LOWER == word) || (FIRST_UPPER == word)
    }
}
