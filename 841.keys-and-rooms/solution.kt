import java.util.Queue

class Solution {
    fun canVisitAllRooms(rooms: List<List<Int>>): Boolean {
        val N = rooms.size
        var seen = BooleanArray(N)
        var remainCnt = N

        val q = LinkedList<Int>()
        q.add(0)
        while(!q.isEmpty() && remainCnt > 0) {
            val curr = q.poll()
            if (seen[curr]) continue
            seen[curr] = true
            remainCnt -= 1

            for (newKey in rooms[curr]) {
                if (seen[newKey]) continue
                q.add(newKey)
            }
        }
        return remainCnt == 0
    }
}
