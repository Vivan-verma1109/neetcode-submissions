class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [float('inf')] * n
        dist[src] = 0

        for i in range(k + 1):
            temp = dist[:]  # copy of current state
            for a, b, price in flights:
                if dist[a] != float('inf') and dist[a] + price < temp[b]:
                    temp[b] = dist[a] + price
            dist = temp

        return dist[dst] if dist[dst] != float('inf') else -1