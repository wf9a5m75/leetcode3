class Solution {
    fun freqAlphabets(s: String): String {
        var i = 0
        var N = s.length
        val result = StringBuilder()
        val baseInt = 'a'.toInt() - 1

        while (i + 2 < N) {

            when {
                s[i + 2] == '#' -> {
                    result.append((Integer.parseInt("${s[i]}${s[i + 1]}") + baseInt).toChar())
                    i += 3
                }
                else -> {
                    result.append((Integer.parseInt("${s[i]}") + baseInt).toChar())
                    i += 1
                }
            }

        }
        while (i < N) {
            result.append((Integer.parseInt("${s[i]}") + baseInt).toChar())
            i += 1
        }
        return result.toString()
    }
}
