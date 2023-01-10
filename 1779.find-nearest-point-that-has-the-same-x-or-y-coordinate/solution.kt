class Solution {
    fun nearestValidPoint(x: Int, y: Int, points: Array<IntArray>): Int {
        var nearestDistance = 999999999.0
        var nearestIdx = -1

        for (i in 0..points.size - 1) {
            val point = points[i]
            if ((point[0] != x) && (point[1] != y)) {
                continue
            }

            val distance = Math.sqrt(
                Math.pow(Math.abs(point[0] - x).toDouble(), 2.0) +
                    Math.pow(Math.abs(point[1] - y).toDouble(), 2.0)
            )

            if (nearestDistance <= distance) {
                continue
            }

            nearestDistance = distance
            nearestIdx = i
        }
        return nearestIdx
    }
}
