type Job = {
  start: number;
  end: number;
  profit: number;
};

function findNextJobIndex(jobs: Job[], start: number, prevJobEndTime: number): number {
  let end = jobs.length - 1;

  while (start <= end) {
      const mid = (start + end) >>> 1;
      if (jobs[mid].start < prevJobEndTime) {
          start = mid + 1;
      } else {
          end = mid - 1;
      }
  }
  return start;
}

function jobScheduling(startTime: number[], endTime: number[], profit: number[]): number {
  const numOfJobs = startTime.length;
  
  const jobs: Job[] = [];
  for (let i = 0; i < numOfJobs; i++) {
      jobs.push({
          start: startTime[i],
          end: endTime[i],
          profit: profit[i],
      });
  }
  jobs.sort((a, b) => a.start - b.start || a.end - b.end);
  

  const dp = new Array(numOfJobs + 1).fill(0);

  for (let i = 0; i < numOfJobs; i++) {
      const nextJobIdx = findNextJobIndex(jobs, i, jobs[i].end);
      dp[nextJobIdx] = Math.max(dp[nextJobIdx], dp[i] + jobs[i].profit);
      dp[i + 1] = Math.max(dp[i + 1], dp[i])
  }
  return dp[numOfJobs];
};