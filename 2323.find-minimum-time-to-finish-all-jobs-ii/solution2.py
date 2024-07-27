from typing import List

class Solution:
    
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        # Assigning small jobs to small workers, large jobs to experts.
        sorted_jobs = sorted(jobs)
        sorted_workers = sorted(workers)

        # We need at least 1 day for any jobs.
        answer = 1
        for job, worker in zip(sorted_jobs, sorted_workers):
            necessary_days = ceil(job / worker)
            answer = max(answer, necessary_days)
        return answer
