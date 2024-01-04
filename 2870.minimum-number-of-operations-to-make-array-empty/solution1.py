#
# DP approach
#   TC: O(N), because we count up
#   SC : O(N), because we count up
#
MAX_INT = 2**30 - 1

class Solution:
    def __init__(self):
        self.cache = collections.defaultdict(int)
        
    def backtrack(self, num: int) -> int:
        if (num in self.cache):
            return self.cache[num]
        
        if (num < 0):
            return MAX_INT
        if (num == 0):
            return 0
        
        by2 = self.backtrack(num - 2)
        by3 = self.backtrack(num - 3)
        self.cache[num] = min(by2, by3) + 1
        return self.cache[num]
    
    def minOperations(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        
        numOfOperation = 0
        
        for count in counts.values():
            if (count == 1):
                return -1
            
            numOfOperation += self.backtrack(count)
            
                
        return numOfOperation
    
