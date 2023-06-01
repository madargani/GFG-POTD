class Solution:
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        visited = [False for i in range(V)]
        sorted_list = []

        for node in range(V):
            self.dfs(node, visited, sorted_list, adj)

        sorted_list.reverse()
        return sorted_list

    def dfs(self, src, visited, sorted_list, adj):
        if visited[src]:
            return
        
        for node in adj[src]:
            self.dfs(node, visited, sorted_list, adj)

        visited[src] = True
        sorted_list.append(src)

a = Solution()

print(a.topoSort(6, [[], [3], [3], [0], [0, 1], [0, 2]]))
