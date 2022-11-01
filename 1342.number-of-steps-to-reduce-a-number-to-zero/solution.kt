class Solution {
    fun numberOfSteps(num: Int): Int {
        var cnt: Int = 0
        var num2: Int = num

        while(num2 > 0) {
            cnt += 1
            if ((num2 and 1) == 1) {
                // Odd
                num2 -= 1
            } else {
                // Even
                num2 = num2 shr 1
            }
        }
        return cnt
    }
}
