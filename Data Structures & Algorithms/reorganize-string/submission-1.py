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
            cnt, ch = heapq.heappop(heap)
            if res and ch == res[-1]:
                cnt2, ch2 = heapq.heappop(heap)
                res.append(ch2)
                cnt2 += 1
                if cnt2 < 0:
                    heapq.heappush(heap, (cnt2, ch2))
                heapq.heappush(heap, (cnt, ch))
            else:
                res.append(ch)
                cnt += 1
                if cnt < 0:
                    heapq.heappush(heap, (cnt, ch))
        return "".join(res)
