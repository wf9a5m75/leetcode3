import java.util.ArrayDeque

class Solution {
    fun allPathsSourceTarget(graph: Array<IntArray>): List<List<Int>> {
        val queues = listOf(
            ArrayDeque<ArrayList<Int>>(),
            ArrayDeque<ArrayList<Int>>()
        )
        var results = ArrayList<List<Int>>()

        var q1Idx = 0
        var q2Idx = 1

        val first = ArrayList<Int>()
        first.add(0)
        queues[q1Idx].add(first)

        val N = graph.size
        while (!queues[q1Idx].isEmpty()) {

            while (!queues[q1Idx].isEmpty()) {
                val currPath = queues[q1Idx].poll()
                val nextV = currPath.get(currPath.size - 1)

                if (nextV == N - 1) {
                    results.add(currPath.toList())
                    continue
                }

                for (v in graph[nextV]) {
                    val newPath = ArrayList<Int>(currPath)
                    newPath.add(v)
                    queues[q2Idx].add(newPath)
                }

            }

            q1Idx = (q1Idx + 1) % 2
            q2Idx = (q2Idx + 1) % 2
        }

        return results.toList()
    }
}
