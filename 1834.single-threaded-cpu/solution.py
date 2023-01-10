class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        results = []
        N = len(tasks)

        # adding each indicies, then sort by enqueue times
        taskList = [(enqeue, process_time, idx) for idx, (enqeue, process_time) in enumerate(tasks)]
        taskList.sort()

        # min heap queue
        hq = []
        curr_time = 0
        i = 0
        while (i < N) or hq:

            # If all tasks less are done before next task,
            # move on to the next task
            if (not hq) and (curr_time < taskList[i][0]):
                curr_time = taskList[i][0]

            # Pick up all tasks less than the current task finish time
            while (i < N) and (taskList[i][0] <= curr_time):
                heapq.heappush(hq, (taskList[i][1], taskList[i][2]))
                i += 1

            # Extends the current task finish time
            poll = heapq.heappop(hq)
            curr_time += poll[0]
            results.append(poll[1])

        return results
