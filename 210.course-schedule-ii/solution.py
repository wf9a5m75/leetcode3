from collections import defaultdict
class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)

        # A pair [a, b] in the input represents edge from b -> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        
        topological_sorted_order = []
        is_possible = True

        # By default all vertices are WHITE (WHITE depicts not visited)
        color = {k: Solution.WHITE for k in range(numCourses)}  # {0: WHITE, 1: WHITE, ..., n: WHITE}

        def dfs(node: int) -> None:
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return
            
            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                        # An edge to a GRAY vertex represents a cycle
                        is_possible = False
            
            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it
            if color[vertex] == Solution.WHITE:
                dfs(vertex)
        
        return topological_sorted_order[::-1] if is_possible else []


            