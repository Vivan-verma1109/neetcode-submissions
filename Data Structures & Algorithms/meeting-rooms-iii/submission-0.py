class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free = []
        busy = []
        count = [0] * n

        for i in range(n):
            heapq.heappush(free, i)
        meetings.sort()

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                ending, room = heapq.heappop(busy)
                heapq.heappush(free, room)
            
            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
                count[room] += 1
            else:
                old_end, room = heapq.heappop(busy)
                new_end = old_end + (end - start)
                heapq.heappush(busy, (new_end, room))
                count[room] += 1
        return count.index(max(count))
