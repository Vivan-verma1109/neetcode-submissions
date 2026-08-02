class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        n = len(edges)
        degree = [0] * (n + 1)

        for i in range(n):
            graph[i + 1] = []

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        print(graph)
        print(degree)

        q = deque()
        for i in range(1, len(degree)):
            if degree[i] == 1:
                q.append(i)
        
        while q:
            node = q.popleft()
            degree[node] -= 1
            for nxt in graph[node]:
                degree[nxt] -= 1
                if degree[nxt] == 1:
                    q.append(nxt)
        
        for a, b in reversed(edges):
            if degree[a] == 2 and degree[b]:
                return [a, b]
        return []






        

