class Solution {
    fun isHappy(n: Int): Boolean {
        var seen = HashSet<Long>()
        var _n: Long = n.toLong()
        var nextN: Long = 0
        var d: Long = 0
        while ((_n != 1L) && (!seen.contains(_n))) {
            seen.add(_n)

            nextN = 0
            while (_n > 0) {
                d = _n % 10
                nextN += d * d
                _n /= 10
            }
            _n = nextN
        }
        return _n == 1L
    }
}
