class Solution {
    fun countOdds(low: Int, high: Int): Int {
        if (low.rem(2) == 0 && high.rem(2) == 0) {
            return (high - low) / 2
        } else {
            return (high - low) / 2 + 1
        }
    }
}
