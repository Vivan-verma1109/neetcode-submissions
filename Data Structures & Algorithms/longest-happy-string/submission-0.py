class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0: heapq.heappush(heap, (-a, 'a'))
        if b > 0: heapq.heappush(heap, (-b, 'b'))
        if c > 0: heapq.heappush(heap, (-c, 'c'))

        res = []

        while heap:
            count, char = heapq.heappop(heap)

            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not heap:
                    return ''.join(res)
                count2, char2 = heapq.heappop(heap)
                res.append(char2)
                count2 += 1
                if count2 < 0:
                    heapq.heappush(heap, (count2, char2))
                heapq.heappush(heap, (count, char))
            else:
                res.append(char)
                count += 1
                if count < 0:
                    heapq.heappush(heap, (count, char))
        return ''.join(res)