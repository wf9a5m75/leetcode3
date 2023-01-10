import kotlin.math.*
class Solution {
    fun nearestValidPoint(x: Int, y: Int, points: Array<IntArray>): Int {
        var minDist = Int.MAX_VALUE
        var minIdx = -1

        points.forEachIndexed lit@{ i, point ->

            if ((point[0] != x) && (point[1] != y)) return@lit

            val dist = abs(point[0] - x) + abs(point[1] - y)
            if (dist < minDist) {
                minDist = dist
                minIdx = i
            }
        }
        return minIdx
    }
}
