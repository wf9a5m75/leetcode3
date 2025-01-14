class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = [
            [inf, 0],
            [inf, 0]
        ]

        for num in nums:
            if votes[0][0] == inf:
                votes[0] = [num, 1]
            elif votes[0][0] == num:
                votes[0][1] += 1
            elif votes[1][0] == inf:
                votes[1] = [num, 1]
            elif votes[1][0] == num:
                votes[1][1] += 1
            else:
                votes[1][1] -= 1
                votes[0][1] -= 1

                if votes[1][1] == 0:
                    votes[1] = [num, 1]
                elif votes[0][1] == 0:
                    votes[0] = [num, 1]
    
        votes[0][1] = 0
        votes[1][1] = 0

        for num in nums:
            if votes[0][0] == num:
                votes[0][1] += 1
            elif votes[1][0] == num:
                votes[1][1] += 1

        if votes[0][1] >= votes[1][1]:
            return votes[0][0]
        else:
            return votes[1][0]