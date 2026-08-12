class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)


        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        comp = 0
        visited = set()

        def dfs(node):
            visited.add(node)

            for nxt in graph[node]:
                if nxt not in visited:
                    dfs(nxt)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                comp += 1
        return comp