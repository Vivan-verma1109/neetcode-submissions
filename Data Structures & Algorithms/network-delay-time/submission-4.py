class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))


        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]


        while heap:
            cost, node = heapq.heappop(heap)

            if cost > dist[node]:
                continue
            
            for nxt, weight in graph[node]:
                newDistance = cost + weight
                if dist[nxt] > newDistance:
                    dist[nxt] = newDistance
                    heapq.heappush(heap, (newDistance, nxt))
        print(dist)
        res = max(dist[1:])
        if res == float("inf"):
            return -1
        return res