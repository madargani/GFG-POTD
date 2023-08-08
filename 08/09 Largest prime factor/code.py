class Solution:
    def largestPrimeFactor (self, N):
        i = 2
        while i ** 2 <= N:
            if N % i == 0:
                N //= i
                continue
            else:
                i += 1
        
        return N

for i in range(2, 101):
    print(f"{i}: {Solution().largestPrimeFactor(i)}")