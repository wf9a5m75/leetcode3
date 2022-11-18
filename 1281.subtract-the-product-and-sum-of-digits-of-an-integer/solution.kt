class Solution {
    fun subtractProductAndSum(n: Int): Int {
        var product = 1
        var sum = 0
        var _n = n
        var _d = 0

        while(_n > 0) {
            _d = _n % 10
            product *= _d
            sum += _d
            _n /= 10
        }
        return product - sum
    }
}
