class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
        while heap:
            res.append(heapq.heappop(heap))
        return (res)