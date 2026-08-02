import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}

        for i in range(n + 1):
            graph[i] = []

        for a, b, weight in times:
            graph[a].append((b, weight))
        dist = {i: float("inf") for i in range(1, n + 1)}
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            curDist, node = heapq.heappop(heap)

            if curDist > dist[node]:
                continue

            for nxt, weight in graph[node]:
                newDist = curDist + weight
            
                if newDist < dist[nxt]:
                    dist[nxt] = newDist
                    heapq.heappush(heap, (newDist, nxt))
        ans = max(dist.values())
        if ans == float("inf"):
            return -1

        return ans