class PossibleNum:
    MIN_INT = -2**31
    
    def __init__(self):
        self.num = PossibleNum.MIN_INT
        self.cnt = 0

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        MIN_INT = -2**31
        possibilities = [PossibleNum(), PossibleNum()]
        halfN = len(nums) >> 1
        
        for i, num in enumerate(nums):
            if possibilities[0].num == num:
                possibilities[0].cnt += 1
            elif possibilities[1].num == num:
                possibilities[1].num += 1
            else:
                possibilities[0].cnt -= 1
                possibilities[1].cnt -= 1
                
                if (possibilities[0].cnt <= 0):
                    possibilities[0] = possibilities[1]
                    possibilities[1] = PossibleNum()
                    
                if (possibilities[0].cnt <= 0):
                    possibilities[0] = possibilities[1]
                    possibilities[1] = PossibleNum()
                
                if (possibilities[0].cnt == 0):
                    possibilities[0].num = num
                    possibilities[0].cnt = 1
                elif (possibilities[1].cnt == 0):
                    possibilities[1].num = num
                    possibilities[1].cnt = 1
        
        possibilities[0].cnt = 0
        possibilities[1].cnt = 0
        for num in nums:
            if num == possibilities[0].num:
                possibilities[0].cnt += 1
                continue
            
            if num == possibilities[1].num:
                possibilities[1].cnt += 1
        
        if (possibilities[0].cnt > halfN):
            return possibilities[0].num
        return possibilities[1].num 