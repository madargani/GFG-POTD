class Solution:
    def LongestRepeatingSubsequence(self, str):
        n = len(str)
	    
        dp = [[0] * n for i in range(n)]
        for i in range(1, n):
            dp[0][i] = dp[i][0] = dp[0][i - 1] or int(str[i] == str[0])
        dp[0][0] = 0
	    
        for i in range(1, n):
            for j in range(1, n):
                if i == j or str[i] != str[j]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    
        # print(*dp, sep='\n')
        return dp[n - 1][n - 1]
    
Solution().LongestRepeatingSubsequence('yvpyruvjhb')