interface Job {
  start: number;
  end: number;
  profit: number;
}

class JobArray extends Array<Job>  {
    
    static fromInputs = (startTime: number[], endTime: number[], profit: number[]): JobArray => {
        const jobArray = new JobArray(startTime.length);
        for (let i = 0; i < startTime.length; i++) {
            jobArray[i] = {
                start: startTime[i],
                end: endTime[i],
                profit: profit[i]
            };
        }
        return jobArray;
    }
    
    sortJobs(): JobArray {
        return this.sort((a, b) => a.start - b.start || a.end - b.end);
    };

    maxProfit(): number {
        const numOfJobs = this.length;
        const dp = new Array(numOfJobs + 1).fill(0)

        for (let i = 0; i < numOfJobs; i++) {
            const nextJobIdx = this.findNextJobIndex(i);
            dp[nextJobIdx] = Math.max(dp[nextJobIdx], dp[i] + this[i].profit);
            dp[i + 1] = Math.max(dp[i + 1], dp[i]);
        }
        return dp[numOfJobs];
    };
    
    private findNextJobIndex(currentIdx: number): number {
        let start = 0;
        let end = this.length - 1;
        const target = this[currentIdx].end;

        while (start <= end) {
            const mid = (start + end) >>> 1;
            if (this[mid].start < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return start;
    }
}


const jobScheduling = (startTime: number[], endTime: number[], profit: number[]): number => {
    return JobArray.fromInputs(startTime, endTime, profit)
        .sortJobs()
        .maxProfit();
};