class Solution:
    def wildCard(self, pattern, string):
        plen, slen = len(pattern), len(string)
        dp = [[False] * slen for _ in range(plen)] # [pi][si]

        for i in range(plen):
            for j in range(slen):
                if pattern[i] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif pattern[i] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = pattern[i] == pattern[j] and dp[i - 1][j - 1]

        return dp[-1][-1]

if __name__ == "__main__":
    ps = []
    ss = []
    for p, s in zip(ps, ss):
        print(Solution().wildCard(p, s))
