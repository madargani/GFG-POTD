class Solution:
    def knapSack(self, W, wt, val):
        dp = [-1] * (W + 1)
        dp[0] = 0

        for w, v in zip(wt, val):
            for i in range(W, w - 1, -1):
                if (dp[i - w] == -1):
                   continue
                dp[i] = max(dp[i], dp[i - w] + v)
        
        print(dp)
        return max(dp)

if __name__ == "__main__":
    W = 4
    wt = [4, 5, 1]
    val = [1, 2, 3]
    Solution().knapSack(W, wt, val)

    
