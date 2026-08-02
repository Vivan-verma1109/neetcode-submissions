class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}

        for i in range(n):
            graph[i] = []

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        print(graph)

        visited = set()
        comp = 0

        def dfs(node):
            visited.add(node)

            for nxt in graph[node]:
                if not nxt in visited:
                    dfs(nxt)
            
        for node in range(n):
            if node not in visited:
                comp += 1
                dfs(node)
        return comp
