class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        options = sorted(zip(capital, profits))
        print(options)
        heap = []
        i = 0
        n = len(options)

        for _ in range(k):
            while i < n and options[i][0] <= w:
                heapq.heappush(heap, -options[i][1])
                i += 1
            
            if not heap:
                break
            
            w += -heapq.heappop(heap)
        return w