import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {}

        for i in range(n):
            graph[i] = []
        
        for a, b, weight in edges:
            graph[a].append((b, weight))

        dist = [float('inf')] * n
        dist[src] = 0

        heap = [(0, src)]
        while heap:
            curDist, node = heapq.heappop(heap)

            if curDist > dist[node]:
                continue
            
            for nxt, cost in graph[node]:
                newDist = cost + curDist
                
                if newDist < dist[nxt]:
                    dist[nxt] = newDist
                    heapq.heappush(heap, (newDist, nxt))
        print(dist)
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
        ans = {}
        for i in range(len(dist)):
            ans[i] = dist[i]
        return ans



