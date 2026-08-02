class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for i in nums:
            if i in s:
                s[i] += 1
            else:
                s[i] = 1
        sort = sorted(s.items(), key=lambda x: x[1], reverse=True)
        print(sort)
        ret = []
        i = 0
        while k != 0:
            ret.append(sort[i][0])
            i += 1
            k -= 1
        return (ret)