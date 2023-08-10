class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        dp = [[0] * y for i in range(x)]
        
        dp[0][0] = int(s1[0] == s2[0])        
        for i in range(1, x):
            dp[i][0] = dp[i - 1][0] or int(s1[i] == s2[0])
        for i in range(1, y):
            dp[0][i] = dp[0][i - 1] or int(s1[0] == s2[i])
        
        for i in range(1, x):
            for j in range(1, y):
                if s1[i] == s2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        print(*dp, sep="\n")
        
a = "prison"
b = "ripson"

Solution().lcs(len(a), len(b), a, b)