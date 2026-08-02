class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a, b = find(a), find(b)        

            if a == b:
                return False

            if rank[a] > rank[b]:
                parent[b] = a
                rank[a] += rank[b]
            else:
                parent[a] = b
                rank[b] += a
            return True


        if len(edges) != n - 1:
            return False

        for a, b in edges:
            if not union(a,b):
                return False
        return True