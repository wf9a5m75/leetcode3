class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacents = [[] for _ in range(numCourses)]
        visited = [False] * numCourses
        inStack = [False] * numCourses

        def dfs(node: int) -> bool:
            if inStack[node]:
                return False
            if visited[node]:
                return True
            
            visited[node] = True
            inStack[node] = True
            for neighbor in adjacents[node]:
                if dfs(neighbor) == False:
                    return False

            inStack[node] = False
            return True
        
        for course, preRequire in prerequisites:
            adjacents[course].append(preRequire)
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True

