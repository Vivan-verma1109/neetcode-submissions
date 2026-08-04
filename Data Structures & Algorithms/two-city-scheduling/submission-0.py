class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0])

        n = len(costs) // 2
        b = costs[:n]
        a = costs[n:]

        tot = 0

        for i in b:
            tot += i[1]

        for i in a:
            tot += i[0]

        return tot