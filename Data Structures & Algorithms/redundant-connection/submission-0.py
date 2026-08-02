class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False
            
            if rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
                rank[rootA] += rank[rootB]
            else:
                parent[rootA] = rootB
                rank[rootB] += rank[rootA]

            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]