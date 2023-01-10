class Solution {
    fun wordPattern(pattern: String, s: String): Boolean {
        val words = s.split(" ")
        if (pattern.length != words.size) return false

        val patternToWord = HashMap<String, String>()
        val wordToPattern = HashMap<String, String>()

        for (i in 0 until words.size) {
            val word = words[i]
            val pChar = pattern[i].toString()
            if (wordToPattern.containsKey(word)) {
                if (pChar != wordToPattern.get(word)) return false

            } else if (patternToWord.containsKey(pChar)) {
                if (word != patternToWord.get(pChar)) return false

            } else {
                patternToWord.put(pChar, word)
                wordToPattern.put(word, pChar)
            }
        }
        return true
    }
}
