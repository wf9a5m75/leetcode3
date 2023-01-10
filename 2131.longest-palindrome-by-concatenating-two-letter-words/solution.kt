class Solution {
    fun longestPalindrome(words: Array<String>): Int {
        val counts = hashMapOf<String, Int>()
        var maxLen = 0
        var center = 0

        for (word in words) {
            val rWord = "${ word[1] }${ word[0] }"

            if (rWord in counts) {
                maxLen += 4

                val n = counts.get(rWord)!! - 1
                if (n == 0) {
                    counts.remove(rWord)
                } else {
                    counts.put(rWord, n)
                }
            } else {
                counts.put(word, (counts.get(word) ?: 0) + 1)
            }
        }

        if (center == 0) {
            for (word in counts.keys) {
                val rWord = "${ word[1] }${ word[0] }"
                if (word == rWord) {
                    center = 2
                    break
                }
            }
        }
        return maxLen + center
    }
}
