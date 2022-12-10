class Solution {
    fun checkStraightLine(coordinates: Array<IntArray>): Boolean {
        val x1 = coordinates[0][0]
        val y1 = coordinates[0][1]
        val x2 = coordinates[1][0]
        val y2 = coordinates[1][1]

        fun isOnTheLine(x: Int, y: Int): Boolean {
            return 0 == (y2 - y1) * (x - x1) - (x2 - x1) * (y - y1)
        }

        for (coord in coordinates) {
            if (!isOnTheLine(coord[0], coord[1])) return false
        }
        return true
    }


}
