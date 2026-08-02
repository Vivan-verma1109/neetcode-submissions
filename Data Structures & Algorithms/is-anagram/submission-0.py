class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        
        for i in s:
            if i in hash_s:
                hash_s[i] += 1
            else:
                hash_s[i] = 1
        
        for i in t:
            if i in hash_t:
                hash_t[i] += 1
            else:
                hash_t[i] = 1
        
        return hash_s == hash_t