from collections import deque

class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        queue = deque()
        dist = [[0] * M for i in range(N)]
        
        queue.append((0, 0))
        dist[0][0] = 1
        while queue:
            cur = queue.popleft()
            if cur == (X, Y):
                return dist[X][Y] - 1

            for x, y in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                x, y = x + cur[0], y + cur[1]
                    
                if 0 <= x < N and 0 <= y < M and A[x][y] and not dist[x][y]:
                    dist[x][y] = dist[cur[0]][cur[1]] + 1
                    queue.append((x, y))
        
        return -1