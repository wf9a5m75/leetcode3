# 2323. Find Minimum Time to Finish All Jobs II
## level: Medium

https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

## problem

You are givin **two 0-indexed** integer array `jobs` and `workers` of equal length, which `jobs[i]` is the amount of time needed to complete the job, and `workers[j]` is the amount of time the `j`th worker can work each day.

Each job should be assigned to **exactly on worker**, such that each worker completes exactly on job.

Return the minimum number of days needed to complete all the jobs after assignment.

## Constraints:
- `n == jobs.length == workers.length`
- `1 <= n <= 1e5`
- `1 <= jobs[i], workers[j] <= 1e5`

## example:

```
Input
  jobs = [5,2,4], workers = [1,7,5]
Output
  2
Explanation:
  - Assign the 2nd worker to the 0th job. It takes them 1 day to finish the job.
  - Assign the 0th worker to the 1st job. It takes them 2 days to finish the job.
  - Assign the 1st worker to the 2nd job. It takes them 1 day to finish the job.
  It takes 2 days for all the jobs to be completed, so return 2.
  It can be proven that 2 days is the minimum number of days needed.
```