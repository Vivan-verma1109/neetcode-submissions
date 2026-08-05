class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        graph = defaultdict(list)
        for a, b, c in times:
            graph[a].append([b, c])

        heap = [(0, k)]
        t = 0

        while heap:
            cost, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            t = max(t, cost)
            visited.add(node)

            for nxt, cost2 in graph[node]:
                if nxt not in visited:
                    heapq.heappush(heap, [(cost2 + cost), nxt])
        return t if len(visited) == n else -1