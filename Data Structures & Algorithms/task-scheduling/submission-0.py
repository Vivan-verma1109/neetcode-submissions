class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        maxf = max(c.values())
        maxCount = 0

        for name, num in c.items():
            if num == maxf:
                maxCount += 1
        print(maxf, maxCount)

        return max(len(tasks), (maxf - 1) * (n + 1) + maxCount)