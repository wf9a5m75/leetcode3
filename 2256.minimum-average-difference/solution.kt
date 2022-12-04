import kotlin.math.*
class Solution {
    fun minimumAverageDifference(nums: IntArray): Int {
        var rightS = 0L
        val numsL = nums.map {
            val itLong = it.toLong()
            rightS += itLong
            itLong
        }

        val N = numsL.size
        var leftS = 0L
        var leftCnt = 0
        var rightCnt = N

        var minIdx = 0
        var minDiff = Long.MAX_VALUE

        for (i in 0 until nums.size) {
            leftCnt += 1
            rightCnt -= 1
            leftS += numsL[i]
            rightS -= numsL[i]

            var diff = abs(when(rightCnt) {
                0 -> leftS / leftCnt
                else -> abs(leftS / leftCnt) - abs(rightS / rightCnt)
            })

            if (diff < minDiff) {
                minDiff = diff
                minIdx = i
            }
        }
        return minIdx
    }
}
