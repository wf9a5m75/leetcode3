class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                # Pick larger counts from the two previous statuses.
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )
                
                if text1[i - 1] != text2[j - 1]:
                    continue
                
                dp[i][j] = max(
                    # do nothing
                    dp[i][j],
                    
                    # if matched, increment the count from the previously matched count
                    dp[i - 1][j - 1] + 1
                )
        
        # for i in range(M + 1):
        #     print(dp[i])
        return dp[M][N]