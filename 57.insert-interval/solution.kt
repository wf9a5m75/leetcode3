class Solution {
    fun insert(intervals: Array<IntArray>, newInterval: IntArray): Array<IntArray> {
        // Sentinels
        val results = intervals.toMutableList()
        results.add(0, intArrayOf(-2, -1))
        results.add(intArrayOf(100001, 100002))

        var N = results.size - 1
        var L = 0
        var R = N - 1
        var mid = 0;
        while (L <= R) {
            mid = (L + R) shr 1
            if (results[mid][0] <= newInterval[0]) {
                L = mid + 1
            } else {
                R = mid - 1
            }
        }

        results.add(L, newInterval)
        N += 1

        L -= 1
        while (L + 1 < N) {
            while ((L + 1 < N) && (results[L][1] >= results[L + 1][0])) {
                N -= 1
                results[L][0] = minOf(results[L][0], results[L + 1][0])
                results[L][1] = maxOf(results[L][1], results[L + 1][1])
                results.removeAt(L + 1)
            }
            L += 1
        }
        results.removeAt(0)
        results.removeAt(N - 1)

        return results.toTypedArray()
    }
}
