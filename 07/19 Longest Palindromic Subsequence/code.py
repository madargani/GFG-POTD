class Solution:
    def longestPalinSubseq(self, S):
        n = len(S)
        s = S[::-1]
        
        dp = [[0] * n for i in range(n)]
        
        dp[0][0] = int(S[0] == s[0])
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] or int(S[0] == s[i])
            dp[i][0] = dp[i - 1][0] or int(S[i] == s[0])
            
        for i in range(1, n):
            for j in range(1, n):
                if S[i] == s[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        # print(*dp, sep="\n")
        return dp[n - 1][n - 1]
        
# hplfsaqqgh
# hgqqasflph
# hqqh
Solution().longestPalinSubseq("hplfsaqqgh")