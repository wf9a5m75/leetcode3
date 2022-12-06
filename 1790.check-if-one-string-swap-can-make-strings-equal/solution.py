class Solution {
    fun areAlmostEqual(s1: String, s2: String): Boolean {
        if (s1 == s2) return true

        val N = s1.length
        var counts = HashMap<Char, Int>()
        var diff = 0

        for (i in 0 until N) {
            val c1 = s1[i]
            val c2 = s2[i]
            counts.put(c1, (counts.get(c1) ?: 0) + 1)
            counts.put(c2, (counts.get(c2) ?: 0) - 1)

            if (c1 == c2) continue
            diff += 1
            if (diff > 2) return false
        }

        for (c in counts.keys) {
            if ((counts.get(c) ?: 0) != 0) return false
        }
        return true
    }
}
