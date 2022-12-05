class Solution {
    fun canMakeArithmeticProgression(arr: IntArray): Boolean {
        arr.sort()
        val diff = arr[1] - arr[0]
        for (i in 1 until arr.size - 1) {
            if (arr[i] + diff != arr[i + 1]) return false
        }
        return true
    }
}
