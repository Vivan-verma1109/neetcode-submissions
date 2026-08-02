class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map_order = {}
        for i, char in enumerate(order):
            map_order[char] = i
    
        def valid(word1, word2):
            for a, b in zip(word1, word2):
                if map_order[a] == map_order[b]:
                    continue
                if map_order[a] < map_order[b]:
                    return True
                else:
                    return False
            if len(word2) < len(word1):
                return False
            return True
        
        for i in range(len(words) - 1):
            print(words[i], words[i + 1])
            if not valid(words[i], words[i + 1]):
                return False
        return True
