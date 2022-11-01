class Solution {
    fun canConstruct(ransomNote: String, magazine: String): Boolean {
        var counts1 = IntArray(26)
        var counts2 = IntArray(26)

        for (c in magazine.iterator()) {
            counts1[c - 'a'] += 1
        }
        for (c in ransomNote.iterator()) {
            counts2[c - 'a'] += 1
        }

        for (i in 0 .. 25) {
            if (counts1[i] < counts2[i]) {
                return false
            }
        }
        return true
    }
}
