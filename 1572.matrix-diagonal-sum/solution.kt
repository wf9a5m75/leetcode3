class Solution {
    fun diagonalSum(mat: Array<IntArray>): Int {
        val N = mat.size
        var s1 = 0
        var s2 = 0
        for (i in 0 until N) {
            s1 += mat[i][i]
            s2 += when(N - i - 1) {
                i -> 0
                else -> mat[i][N - i - 1]
            }
        }
        return s1 + s2
    }
}
