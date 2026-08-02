class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}

        for i in range(len(edges)):
            graph[i + 1] = []
        
        def connected(node, target, visited):
            if node in visited:
                return False
            if node == target: 
                return True
            visited.add(node)
            for nxt in graph[node]:
                if connected(nxt, target, visited):
                    return True
            return False



        for a, b in edges:
            if connected(a,b, set()): return [a,b]
            graph[a].append(b)
            graph[b].append(a)
            
    

        

