from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        # adj[a] - edges from node x
        # adj[a][b][0] - to node of edge
        # adj[a][b][1] - distance of edge
        adj = [[] for i in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1:])
            
        dist = [-1] * n
        dist[0] = 0
        
        order = self.topOrder(n, adj)
        for node in order:
            if dist[node] == -1:
                continue
            for to_node, cost in adj[node]:
                if dist[to_node] == -1:
                    dist[to_node] = dist[node] + cost
                else:
                    dist[to_node] = min(dist[to_node], dist[node] + cost)
                    
        return dist       
    
    def topOrder(self, n, adj):
        order = []
        
        in_degree = [0] * n
        for edges in adj:
            for to_node, _ in edges:
                in_degree[to_node] += 1
        
        ready = {i for i in range(n) if in_degree[i] == 0}
        
        while ready:
            cur = ready.pop()
            order.append(cur)
            for to_node, _ in adj[cur]:
                in_degree[to_node] -= 1
                if in_degree[to_node] == 0:
                    ready.add(to_node)
                    
        return order
        
            
            