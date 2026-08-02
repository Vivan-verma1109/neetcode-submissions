class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
        res = []
        for i in range(len(heap)):
            res.append((heapq.heappop(heap)))
        return (res)