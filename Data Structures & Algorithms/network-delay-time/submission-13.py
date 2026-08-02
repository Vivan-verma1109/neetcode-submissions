import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for a,b,weight in times:
            graph[a].append((b, weight))

        heap = [(0, k)]
        t = 0
        visited = set()

        while heap:
            w1, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited.add(node)

            t = max(t, w1)

            for nxt, w2 in graph[node]:
                if nxt not in visited:
                    heapq.heappush(heap, (w2 + w1, nxt))
        return t if len(visited) == n else -1
            