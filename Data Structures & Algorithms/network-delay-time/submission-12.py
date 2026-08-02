import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for a, b, weight in times:
            graph[a].append((b, weight))

        heap = [(0, k)]
        t = 0
        visited = set()

        while heap:
            weight, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            t = max(t, weight)
            visited.add(node)

            for nxt, w2 in graph[node]:
                if nxt not in visited:
                    heapq.heappush(heap, (w2 + weight, nxt))
        return t if len(visited) == n else -1
                    