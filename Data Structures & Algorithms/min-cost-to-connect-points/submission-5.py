class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        n = len(points)
        dist = [float('inf')] * n
        dist[0] = 0

        total = 0

        for _ in range(n):
            node = -1

            for i in range(n):
                if i not in visited and (node == -1 or dist[i] < dist[node]):
                    node = i
            visited.add(node)
            total += dist[node]

            for nxt in range(n):
                if nxt not in visited:
                    distance = abs(points[node][0] - points[nxt][0]) + abs(points[node][1] - points[nxt][1])
                    dist[nxt] = min(distance, dist[nxt])
        return total
