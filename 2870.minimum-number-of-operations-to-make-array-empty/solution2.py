# Greedy
#   TC: O(N), because we count up
#   SC : O(N), because we count up
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        
        numOfOperation = 0
        
        for count in counts.values():
            if (count == 1):
                return -1
            
            # Equivalents with the below code
            numOfOperation += math.ceil(count / 3)
            
            # if (count % 3 == 0):
            #     numOfOperation += count // 3
            # else:
            #     numOfOperation += count // 3 + 1
            
        return numOfOperation
