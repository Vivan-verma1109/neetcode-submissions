from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)

        q = deque(s2[:len(s1)])
        window = Counter(q)

        if window == need:
            return True

        for ch in s2[len(s1):]:
            left = q.popleft()
            window[left] -= 1

            if window[left] == 0:
                del window[left]

            q.append(ch)
            window[ch] += 1

            if window == need:
                return True
        return False