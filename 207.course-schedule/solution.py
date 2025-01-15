class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjacents = [[] for _ in range(numCourses)]

        for course, reqCourse in prerequisites:
            adjacents[reqCourse].append(course)
            indegree[course] += 1
        
        q = deque()
        # pick up the start position courses
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        nodesVisited = 0
        while q:
            node = q.popleft()
            nodesVisited += 1

            for neighbor in adjacents[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return nodesVisited == numCourses

