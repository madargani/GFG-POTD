class Solution:
    def FirstNonRepeating(self, A):
        freqs = {}
        first = 0
        res = ""
        for i, x in enumerate(A):
            if x not in freqs:
                freqs[x] = 0
            freqs[x] += 1
            
            while first <= i and freqs[A[first]] > 1:
                first += 1
                
            if first > i:
                res += "#"
            else:
                res += A[first]
        return res

print(Solution().FirstNonRepeating("aabc"))
        