class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}

        for i in range(n):
            graph[i] = []
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        print(graph)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                if not dfs(nxt, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visited) == n