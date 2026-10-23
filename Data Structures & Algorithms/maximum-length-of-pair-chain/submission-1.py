class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        print(pairs)

        end = pairs[0][1]
        count = 1
        for i in range(1, len(pairs)):
            if pairs[i][0] > end:
                end = max(end, pairs[i][0])
                count += 1
        return (count)
