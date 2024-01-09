interface Job {
  start: number
  end: number
  profit: number
}

class JobArray extends Array<Job> {
  public maximumProfit (): number {
    const scores = new Array(this.length + 1)
    scores[this.length] = 0
    for (let i = this.length - 1; i >= 0; i--) {
      scores[i] = Math.max(this[i].profit + scores[this.findNextJobIndex(i)], scores[i + 1])
    }
    return scores[0]
  }

  public findNextJobIndex (low: number): number { 
    const target = this[low].end
    let high = this.length
    while (low < high) {
      const mid = (low + high) >>> 1
      if (this[mid].start < target) low = mid + 1
      else high = mid
    }
    return high
  }

  public sortBySchedules (): JobArray {
    return this.sort((a, b) => a.start - b.start || a.end - b.end)
  }

  public static fromInputs (starts: number[], ends: number[], profits: number[]): JobArray {
    const output = new JobArray(starts.length)
    for (let i = 0, bound = starts.length; i < bound; i++) {
      output[i] = { start: starts[i], end: ends[i], profit: profits[i] }
    }
    return output
  }
}

const jobScheduling = (starts: number[], ends: number[], profits: number[]): number => {
  return JobArray.fromInputs(starts, ends, profits).sortBySchedules().maximumProfit()
}