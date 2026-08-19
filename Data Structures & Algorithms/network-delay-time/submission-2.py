class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for node, dest, weight in times:
            graph[node].append([dest, weight])
        
        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]
        t = 0


        while heap:
            current_distance, node = heapq.heappop(heap)

            if current_distance > dist[node]:
                continue
            for nxt, cost in graph[node]:
                new_distance = current_distance + cost
                if new_distance < dist[nxt]:
                    dist[nxt] = new_distance
                    heapq.heappush(heap, [new_distance, nxt])
        
        print(dist)
        res = max(dist[1:])
        if res == float("inf"):
            return -1
        return res
