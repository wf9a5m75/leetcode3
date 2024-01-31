class Schedule {
    final int start;
    final int end;
    final int profit; 
    Schedule(int start, int end, int profit) {
        this.start = start;
        this.end = end;
        this.profit = profit;
    }
    
    public static final Comparator<Schedule> Comparator = new Comparator<>() {
        
        @Override
        public int compare(Schedule s1, Schedule s2) {
            return s1.start - s2.start;
        }
    };
}
class Solution {
    
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int N = startTime.length;
        Schedule[] schedules = new Schedule[N];
        for (int i = 0; i < N; i++) {
            schedules[i] = new Schedule(
                startTime[i],
                endTime[i],
                profit[i]
            );
        }
        Arrays.sort(schedules, Schedule.Comparator);
        
        int[] dp = new int[N + 1];
        for (int i = 0; i < N; i++) {
            // do nothing
            dp[i + 1] = Math.max(dp[i + 1], dp[i]);
            
            // do something
            int nextIdx = this.findNextScheduleIndex(schedules, i);
            dp[nextIdx] = Math.max(dp[nextIdx], dp[i] + schedules[i].profit);
        }
        return dp[N];
    }
    
    private int findNextScheduleIndex(Schedule[] schedules, int currentIdx) {
        int L = currentIdx;
        int R = schedules.length - 1;
        int target = schedules[currentIdx].end;
        
        while (L <= R) {
            int mid = (L + R) >> 1;
            if (schedules[mid].start < target) {
                L = mid + 1;
            } else {
                R = mid - 1;
            }
        }
        return L;
    }
}