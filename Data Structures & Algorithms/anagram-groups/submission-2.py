class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)

        for i in range(len(strs)):
             s1 = ("".join(sorted(strs[i])))
             g[s1] = []
        print(g)

        for i in strs:
            temp = i
            s1 = ("".join(sorted(i)))
            g[s1].append(temp)
        print(g)
        res = []

        for i in g.values():
            res.append(i)
        return (res)                
                