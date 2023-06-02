class Solution:
    primes = []

    def precompute(self):
        n = 1299709 #10^5 prime
        prime = [True] * (n + 1)

        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        for p in range(2, n + 1):
            if prime[p]:
                self.primes.append(p)
    
    def helpSanta(self, n, m, g):
        if not m:
            return -1
        
        visited = [False] * (n + 1)

        max_size = 0
        for i in range(1, n + 1):
            if visited[i]:
                continue

            stack = [i]
            visited[i] = True
            size = 0
            while len(stack) > 0:
                cur = stack.pop()
                size += 1

                for node in g[cur]:
                    if not visited[node]:
                        visited[node] = True
                        stack.append(node)
            max_size = max(max_size, size)

        return self.primes[max_size - 1]
        

N = 10
M = 6
G = [[], [2], [1, 3], [2, 4], [3, 5], [4], [7], [6], [], [10], [9]]

obj = Solution()
obj.precompute()
print(obj.helpSanta(N, M, G))