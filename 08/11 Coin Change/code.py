class Solution:
    def count(self, coins, N, Sum):
        dp = [1] + [0] * Sum
        for coin in coins:
            for i in range(1, Sum + 1):
                if coin <= i:
                    dp[i] += dp[i - coin]
        return dp[Sum]   
 
print(Solution().count([1, 2, 3], 3, 4))