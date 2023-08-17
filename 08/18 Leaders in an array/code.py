class Solution:
    def leaders(self, A, N):
        ans = []
        right_max = -1
        for i in reversed(A):
            if i >= right_max:
                ans.append(i)
                right_max = i
        return reversed(ans)