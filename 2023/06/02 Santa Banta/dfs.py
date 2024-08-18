import sys

sys.setrecursionlimit(100000)

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
        visited = [False] * (n + 1)

        max_ = 0
        for i in range(n):
            max_ = max(max_, self.dfs(i, visited, g))
        
        return self.primes[max_ - 1]

    def dfs(self, src, visited, adj):
        if visited[src]:
            return 0
        visited[src] = True
        sum = 1
        for node in adj[src]:
            sum += self.dfs(node, visited, adj)
        return sum
        

N = 10
M = 6
G = [[1,2],[2,3],[3,4],[4,5],[6,7],[9,10]]

obj = Solution()
obj.precompute()
print(obj.helpSanta(N, M, G))