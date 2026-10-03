import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        stored = 0
        for num in nums:
            heapq.heappush(heap, -num)

        while k != 0:
            stored = heapq.heappop(heap)
            k -= 1

        return abs(stored)