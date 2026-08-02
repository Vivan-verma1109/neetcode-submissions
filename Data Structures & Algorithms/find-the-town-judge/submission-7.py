class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # so a hjudge has to be not be in set trust and not be in set trusting
        # [[1,2]] so 1 trusts 2, 1 in trusting 2 in trusted, 2 trusts no one, so 
        # 2 is in trusted but not in trusting
        trusted = [0] * (n + 1)
        trusting = set()

        for a, b in trust:
            trusted[b] += 1
            trusting.add(a)
        print(trusted)

        for i in range(1, n + 1):
            if trusted[i] == n - 1 and i not in trusting:
                return i
        return -1
