class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        # sort by enqueue time, process time and index
        taskList = []
        for i, task in enumerate(tasks):
            taskList.append([task[0], task[1], i])
        heapq.heapify(taskList)
        
        firstTask = heapq.heappop(taskList)
        currTaskEnd = firstTask[0] + firstTask[1]
        results = [firstTask[2]] # index
        
        # keep available task
        buff = []
        
        while True:
            
            # Skip the currTaskEnd
            # if no available tasks and currTaskEnd is smaller than taskList[0][0]
            if (len(buff) == 0) and (taskList) and (taskList[0][0] > currTaskEnd):
                #print(f"<skip> {currTaskEnd} -> {taskList[0][0]}")
                currTaskEnd = taskList[0][0]
            
            # pick up tasks enqueued tasks before currTaskEnd
            while (taskList) and (taskList[0][0] <= currTaskEnd):
                task = heapq.heappop(taskList)
                heapq.heappush(buff, [task[1], task[2]])
            
            # If no available task for next loading,
            # we can stop the loop (we complete all tasks)
            if (len(buff) == 0):
                break
                
            # print(currTaskEnd, buff)
            
            # Pick the next smallest process time task
            nextTask = heapq.heappop(buff)
            currTaskEnd += nextTask[0] # processTime
            results.append(nextTask[1]) # index
        
        return results
   