class Majority:
    def __init__(self, item: int = None):
        self.item = item
        self.count = 0
    def __repr__(self):
        return f"(item:{self.item}, cnt: {self.count})"

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majorities = [Majority(), Majority(), Majority()]
        for num in nums:
            hit = False
            for majority in majorities:
                if majority.item == num:
                    majority.count += 1
                    hit = True
                    break
            if hit:
                continue
            
            for majority in majorities:
                if majority.item is not None:
                    continue

                majority.count = 1
                majority.item = num
                hit = True
                break
                
            if hit:
                continue
            
            for majority in majorities:
                majority.count -= 1
                if (majority.count > 0):
                    continue
                majority.item = None
        
        majorities[0].count = 0
        majorities[1].count = 0
        majorities[2].count = 0
        for num in nums:
            for majority in majorities:
                if majority.item != num:
                    continue
                majority.count += 1
                break
        
        results = []
        threathold = len(nums) / 3
        for majority in majorities:
            if majority.count <= threathold:
                continue
            results.append(majority.item)
        return results