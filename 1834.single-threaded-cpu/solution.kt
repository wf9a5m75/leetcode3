import java.util.PriorityQueue
import java.util.Comparator
data class Task(
    val enqueue: Int,
    val processTime: Int,
    val idx: Int
)
class Solution {
    fun getOrder(tasks: Array<IntArray>): IntArray {

        val results = ArrayList<Int>()
        val taskList = ArrayList<Task>()
        tasks.forEachIndexed { idx, task -> taskList.add(Task(
            task[0],
            task[1],
            idx
        ))}

        // sort by enqueue time
        taskList.sortWith( compareBy { it.enqueue })

        var i = 0
        var taskFinishTime = 0
        var heapQ = PriorityQueue<Task>( compareBy { it: Task -> it.processTime }.thenBy { it: Task -> it.idx })
        val N = taskList.size

        while ((i < N) || (!heapQ.isEmpty())) {
            if (heapQ.isEmpty() &&(taskFinishTime <= taskList.get(i).enqueue)) {
                taskFinishTime = taskList.get(i).enqueue
            }

            while ((i < N) && (taskList.get(i).enqueue <= taskFinishTime)) {
                heapQ.add(taskList.get(i))
                i += 1
            }

            val poll = heapQ.poll()
            taskFinishTime += poll.processTime
            results.add(poll.idx)
        }

        return results.toIntArray()
    }
}
