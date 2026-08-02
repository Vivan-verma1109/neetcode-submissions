class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # so a hjudge has to be not be in set trust and not be in set trusting
        # [[1,2]] so 1 trusts 2, 1 in trusting 2 in trusted, 2 trusts no one, so 
        # 2 is in trusted but not in trusting
        trusted = defaultdict(list)
        trusting = set()

        for a, b in trust:
            trusted[b].append(a)
            trusting.add(a)

        for a, b in trusted.items():
            print(a, b)
            if a not in trusting and len(b) == n - 1:
                return a
        return -1
