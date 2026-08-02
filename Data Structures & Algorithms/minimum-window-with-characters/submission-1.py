class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)

        best = ""

        for i in range(len(s)):
            window = Counter()

            for j in range(i, len(s)):
                window[s[j]] += 1

                valid = True

                for c in need:
                    if window[c] < need[c]:
                        valid = False
                        break

                if valid:
                    curr = s[i:j+1]

                    if best == "" or len(curr) < len(best):
                        best = curr

                    break

        return best