class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        n = len(points)

        minDist = [float('inf')] * n
        minDist[0] = 0

        total = 0

        for _ in range(n):
            node = -1

            for i in range(n):
                if i not in visited and (node == -1 or minDist[i] < minDist[node]):
                    node = i
                
            visited.add(node)
            total += minDist[node]

            for nxt in range(n):
                if nxt not in visited:
                    dist = abs(points[node][0] - points[nxt][0]) + abs(points[node][1] - points[nxt][1])
                    minDist[nxt] = min(minDist[nxt], dist)
        return total
