class Solution:
    def average(self, salary: List[int]) -> float:
        lowest = 10000000
        highest = 0
        total = 0
        for s in salary:
            lowest = min(lowest, s)
            highest = max(highest, s)
            total += s

        return (total - lowest - highest) / (len(salary) - 2)
