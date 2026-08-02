class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
            
        while len(heap) > 1:
            l = heapq.heappop(heap)
            r = heapq.heappop(heap)
            if l == r:
                continue
            if abs(l) - abs(r):
                heapq.heappush(heap, l - r)
        if len(heap) == 0:
            return 0
        return abs(heapq.heappop(heap))
