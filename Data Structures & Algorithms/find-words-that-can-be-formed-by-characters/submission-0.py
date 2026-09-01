class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        total = 0

        for word in words:
            w = Counter(word)
            good = True

            for item, val in w.items():
                if val > c[item]:
                    good = False
                    break

            if good:
                total += len(word)

        return total