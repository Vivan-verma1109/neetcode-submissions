class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(words[0])

        for w in words:
            w = Counter(w)
            for i in c:
                c[i] = min(c[i], w[i])
        res = []
        for i in c:
            for j in range(c[i]):
                res.append(i)
        return res