class Solution {
    fun minimumRounds(tasks: IntArray): Int {
        val counts = HashMap<Int, Int>()
        var result = 0

        // Counts up each taskId
        for (taskId in tasks) {
            counts.put(taskId, (counts.get(taskId) ?: 0) + 1)
        }

        // Calculates the rounds
        for (taskId in counts.keys) {
            val taskCnt = counts.get(taskId) ?: 1
            if (taskCnt == 1) return -1

            val div2 = (taskCnt / 2) + (taskCnt % 2)
            val div3 = (taskCnt / 3) + when(taskCnt % 3) {
                0 -> 0
                else -> 1
            }
            result += minOf(div2, div3)
        }

        return result
    }
}
