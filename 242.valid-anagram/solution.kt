class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        if (s.length != t.length) return false

        var counts = ArrayList<Int>()
        for (i in 0 .. 25) {
            counts.add(0)
        }

        val aOrd = 'a'.toInt()
        for (i in 0 until s.length) {
            counts[s[i].toInt() - aOrd]++
        }
        for (i in 0 until t.length) {
            counts[t[i].toInt() - aOrd]--
        }
        for (i in 0..25) {
            if (counts[i] != 0) return false
        }
        return true
    }
}
