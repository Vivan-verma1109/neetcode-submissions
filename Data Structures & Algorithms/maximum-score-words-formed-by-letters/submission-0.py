class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        available = [0] * 26
        best = float("-inf")
        for c in letters:
            available[ord(c)-97] += 1

        def backtrack(i, path):
            nonlocal best
            if i == len(words):
                total = 0
                for j in path:
                    for y in j:
                        total += score[ord(y) - 97]
                best = max(total, best)
                return best

            backtrack(i + 1, path)
            flag = True
            for c in words[i]:
                available[ord(c) - 97] -= 1
                if available[ord(c) - 97] < 0:
                    flag = False
            
            if flag:
                path.append(words[i])
                backtrack(i + 1, path)
                path.pop()
            for c in words[i]:
                available[ord(c) - 97] += 1
        
        backtrack(0, [])
        return best
