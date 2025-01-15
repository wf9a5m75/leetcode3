class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacents = [[] for _ in range(numCourses)]
        for course, preCourse in prerequisites:
            adjacents[preCourse].append(course)
        
        visited = [False] * numCourses
        inStack = [False] * numCourses
        for i in range(numCourses):
            if self.dfs(i, adjacents, visited, inStack):
                return False
        return True
    
    def dfs(self, node: int, adjacents: List[List[int]], visited: List[bool], inStack: List[bool]) -> bool:
        # If the node is already in stack, we have a cycle
        if inStack[node]:
            return True
        
        if visited[node]:
            return False
        
        # Mark the curret node as visited and part of current recursion stack.
        visited[node] = True
        inStack[node] = True
        for neighbor in adjacents[node]:
            if self.dfs(neighbor, adjacents, visited, inStack):
                return True
        # Remove the node from the stack
        inStack[node] = False
        return False