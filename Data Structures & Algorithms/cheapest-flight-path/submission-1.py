class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = {}

        for i in range(n):
            graph[i] = []

        for a, b, price in flights:
           graph[a].append((b, price))
        
        prices = [float("inf")] * n
        prices[src] = 0

        q = deque([(src, 0)])

        stops = 0

        while q and stops <= k:
            size = len(q)

            temp = prices.copy()

            for _ in range(size):
                node, cost = q.popleft()

                for nxt, price in graph[node]:
                    newCost = price + cost
                    if newCost < temp[nxt]:
                        temp[nxt] = newCost
                        q.append([nxt, newCost])
            prices = temp
            stops += 1
        return prices[dst] if prices[dst] != float("inf") else -1

