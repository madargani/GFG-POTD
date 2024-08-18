class Solution:
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        indegree = [0]*V
        for i in adj:
            for j in i:
                indegree[j] += 1

        stack = [i for i in range(V) if indegree[i] == 0]
        
        res = []
        while stack:
            last = stack.pop()
            res.append(last)
            for node in adj[last]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    stack.append(node)

        return res

a = Solution()
print(a.topoSort(6, [[], [3], [3], [0], [0, 1], [0, 2]]))
