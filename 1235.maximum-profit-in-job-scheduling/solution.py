class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        
        jobs = [
            {
                "start": startTime[i],
                "end": endTime[i],
                "profit": profit[i],
            } for i in range(N)
        ]
        
        # ジョブを開始時間順に並び替える
        jobs.sort(key = cmp_to_key(lambda x, y: x["start"] - y["start"]))
                  
        dp = {}
        def findNextJobIndex(currentEndTime: int) -> int:
            start = 0
            end = N - 1
            idx = N
            while (start <= end):
                mid = (start + end) >> 1
                if (jobs[mid]["start"] >= currentEndTime):
                    end = mid - 1
                    idx = mid
                else:
                    start = mid + 1
            return idx
            
        def backtrack(position: int) -> int:
            if (position == N):
                return 0
                  
            if (position in dp):
                return dp[position]
            
            # jobs[position] を選択しない場合
            doNothing = backtrack(position + 1)
            
            # jobs[position] を選択するとして、次の開始位置を探す
            nextIdx = findNextJobIndex(jobs[position]["end"])
            
            # jobs[nextIdx] から探索を始める
            doJob = backtrack(nextIdx) + jobs[position]["profit"]
            
            dp[position] = max(doNothing, doJob)
            return dp[position]
        
        return backtrack(0)