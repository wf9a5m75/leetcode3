# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class PalindromDetector:
    def __init__(self):
        self.__counts = [0] * 10
        self.__isPalindrome = False
    
    def add(self, val: int):
        self.__counts[val] += 1
        self.__update()
    
    def remove(self, val: int):
        self.__counts[val] -= 1
        self.__update()
    
    def __update(self):
        oddCnt = 0
        evenCnt = 0
        for i, val in enumerate(self.__counts):
            if (val == 0):
                continue
            if (val % 2 == 0):
                evenCnt += 1
            else:
                oddCnt += 1
        
        self.__isPalindrome = False
        if (oddCnt == 0):
            #print(self.__counts, f"oddCnt={oddCnt}, evenCnt={evenCnt}")
            self.__isPalindrome = evenCnt > 0
            return
        
        if (oddCnt == 1):
            #print(self.__counts, f"oddCnt={oddCnt}, evenCnt={evenCnt}", True)
            self.__isPalindrome = True
        
    @property
    def isPalindrome(self):
        return self.__isPalindrome
    
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0
        return self.backtrack(root, PalindromDetector())
        
    def backtrack(self, curr: TreeNode, detector: PalindromDetector) -> int:
        
        detector.add(curr.val)
        result = 0
        if (curr.left or curr.right):
            if (curr.left):
                result += self.backtrack(curr.left, detector)
            if (curr.right):
                result += self.backtrack(curr.right, detector)
        else:
            result = 1 if detector.isPalindrome else 0
            
        detector.remove(curr.val)
        
        return result
        