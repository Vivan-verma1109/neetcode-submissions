class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        active = set()
        res = []

        length = 0

        for ch in s:
            length += 1

            active.add(ch)
            count[ch] -= 1

            if count[ch] == 0:
                active.remove(ch)

            if not active:
                res.append(length)
                length = 0

        return res