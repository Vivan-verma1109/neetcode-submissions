class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(len(edges)):
            graph[i + 1] = []

        def verify(node, target, visited):
            if node in visited:
                return False
            if node == target:
                return True
            visited.add(node)
            for nxt in graph[node]:
                if verify(nxt, target, visited):
                    return True
            return False


        
        for a, b in edges:
            if verify(a, b, set()):
                 return [a,b]
            graph[a].append(b)
            graph[b].append(a)