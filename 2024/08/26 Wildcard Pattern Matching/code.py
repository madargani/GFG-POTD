class Solution:
    def wildCard(self, pattern, string):
        string = '#' + string
        dp = [[False] * (len(string) + 1) for _ in range(len(pattern) + 1)] # [patternIndex][stringIndex]
        dp[0][1] = True

        for pi, pc in enumerate(pattern, start=1):
            for si, sc in enumerate(string, start=1):
                if pc == '*':
                    dp[pi][si] = dp[pi - 1][si - 1] or dp[pi - 1][si] or dp[pi][si - 1]
                elif pc == '?':
                    dp[pi][si] = dp[pi - 1][si - 1]
                else:
                    dp[pi][si] = dp[pi - 1][si - 1] and pc == sc

        return dp[-1][-1]

if __name__ == "__main__":
    ps = ['?*?', '*b*']
    ss = ['a', 'b']
    for p, s in zip(ps, ss):
        print(Solution().wildCard(p, s))

'''
 #a
#10
?01
*11
?11
'''
