class Solution {
    fun canConstruct(ransomNote: String, magazine: String): Boolean {
        var counts = IntArray(size = 26)

        for (c in magazine.toCharArray()) {
            counts[c - 'a'] += 1
        }
        // println(counts.toList())

        for (c in ransomNote) {
            if (--counts[c - 'a'] == -1) {
                return false
            }
        }
        return true
    }
}
