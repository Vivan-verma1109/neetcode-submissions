class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, 0)]
        visited = set()
        n = len(points)
        total = 0

        while heap:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            total += cost

            for nxt in range(n):
                if nxt not in visited:
                    distance = abs(points[node][0] - points[nxt][0]) + abs(points[node][1] - points[nxt][1])
                    heapq.heappush(heap, (distance, nxt))
        return total
