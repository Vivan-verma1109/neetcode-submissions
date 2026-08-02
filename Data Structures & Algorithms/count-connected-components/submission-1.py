class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a,b):
            a, b = find(a), find(b)

            if a == b:
                return 0
            
            if rank[a] > rank[b]:
                parent[b] = a
                rank[a] += rank[b]
            else:
                parent[a] = b
                rank[b] += rank[a]
            return 1
        res = n
        for a, b in edges:
            res -= union(a, b)
        return res
        
