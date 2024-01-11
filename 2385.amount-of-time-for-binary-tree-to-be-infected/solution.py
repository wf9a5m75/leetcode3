# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Vertix:
    def __init__(self, val: int):
        self.val = val
        self.edges = []
        
class Solution:
    def infectCounter(self, vertix: Vertix) -> int:
        visited = set()
        q = collections.deque([(vertix, 0)])
        result = 0
        while q:
            v, cnt = q.popleft()
            if (v.val in visited):
                continue
            result = max(result, cnt)
            
            visited.add(v.val)
            for nextV in v.edges:
                if (nextV in visited):
                    continue
                q.append([nextV, cnt + 1])
        return result
            
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        graph = {}
        
        def makeGraph(otherVertix: Vertix, node: Optional[TreeNode]):
            if (node is None):
                return
            myVertix = Vertix(node.val)
            graph[node.val] = myVertix
            otherVertix.edges.append(myVertix)
            myVertix.edges.append(otherVertix)
            
            makeGraph(myVertix, node.left)
            makeGraph(myVertix, node.right)
        
        rootV = Vertix(root.val)
        makeGraph(rootV, root)
        
        return self.infectCounter(graph[start])
        