class Solution:
    def leastPrimeFactor(self, n):
        primes = [0] * (n + 1)
        primes[1] = 1
        for i in range(2, n + 1):
            if primes[i]:
                continue
            for j in range(i, n + 1, i):
                if not primes[j]:
                    primes[j] = i
        return primes


print(Solution().leastPrimeFactor(20))
