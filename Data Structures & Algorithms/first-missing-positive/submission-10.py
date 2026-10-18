class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        need = 1
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
        
        while heap[0] < 0:
            heapq.heappop(heap)
        print(heap)

        while heap:
            top = heapq.heappop(heap)
            if top < need:
                continue
            if top == need:
                need += 1
            else:
                return need
        
        return need

        
