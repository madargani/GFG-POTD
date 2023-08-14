class Solution:
    def maxOnes(self, a, n):
        best = 0
        cur = 0
        for bit in a:
            if not bit:
                cur += 1
                best = max(best, cur)
            else:
                if cur > 0:
                    cur -= 1
        return sum(a) + best
                
            

a = [int(x) for x in "1001001"]
n = len(a)
print(Solution().maxOnes(a, n))