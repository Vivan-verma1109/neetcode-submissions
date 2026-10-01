class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        if max(c.values()) > (len(s) + 1) // 2:
            return ""
        
        heap = []

        for letter, i in c.items():
            heapq.heappush(heap, (-i, letter))
        
        res = []
        while heap:
            count, char = heapq.heappop(heap)

            if res and res[-1] == char:
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
        return "".join(res)