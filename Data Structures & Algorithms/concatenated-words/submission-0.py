class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        w = set(words)
        res = []

        for word in words:
            dp = [False] * (len(word) + 1)
            count = [0] * (len(word) + 1) 

            dp[0] = True

            for i in range(1, len(word) + 1):
                for j in range(0, i):
                    if dp[j] and word[j : i] in w:
                        dp[i] = True
                        count[i] = count[j] + 1
            if dp[len(word)] and count[len(word)] >= 2:
                res.append(word)
        return res