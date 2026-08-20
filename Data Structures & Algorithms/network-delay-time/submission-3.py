class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        res = max(dist[1:])
        if res == float("inf"):
            return -1
        return res