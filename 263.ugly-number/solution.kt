class Solution {
    fun isUgly(n: Int): Boolean {
        var mutableN = n

        // Remove 2,3,5 factors from n
        for (factor in listOf(2,3,5)) {
            while ((mutableN > 1) && (mutableN % factor == 0)) {
                mutableN /= factor
            }
        }

        // n should be 1.
        // Otherwise, n still contains another factor
        return mutableN == 1
    }

}
