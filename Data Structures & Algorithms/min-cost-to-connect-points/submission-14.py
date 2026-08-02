import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        heap = [(0, 0)]
        total = 0

        while len(visited) < n:
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
