from fractions import Fraction
from typing import List

class Solution:

    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        """
        Assign each work in order of workload and worker ability.
        """
        sorted_jobs = list(sorted(jobs))
        sorted_workers = list(sorted(workers))

        necessary_days = 1
        for job, worker in zip(sorted_jobs, sorted_workers):
            frac = Fraction(job, worker)

            days_to_complete = 0
            if frac.numerator < frac.denominator:
                days_to_complete = 1
            elif frac.denominator == 1:
                days_to_complete = frac.numerator
            else:
                days_to_complete = int(frac.numerator / frac.denominator) + 1
            
            necessary_days = max(necessary_days, days_to_complete)
        
        return necessary_days
