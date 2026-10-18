class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        need = 1
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
        if max(heap) < 0:
            return need
        while heap[0] < 0:
            heapq.heappop(heap)
        while heap:
            top = heapq.heappop(heap)
            if top < need:
                continue
            if top == need:
                need += 1
            else:
                return need
        
        return need

        
