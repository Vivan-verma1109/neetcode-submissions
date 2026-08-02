class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = []

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            valid.append([a, b, c])
        print(valid)

        a = []
        b = []
        c = []

        if not valid:
            return False

        for x,y,z in valid:
            a.append(x)
            b.append(y)
            c.append(z)
        fin = [max(a), max(b), max(c)]
        return fin == target