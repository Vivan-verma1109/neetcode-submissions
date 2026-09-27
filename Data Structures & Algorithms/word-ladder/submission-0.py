class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)
        visited = set()
        visited.add(beginWord)
        q = deque()
        q.append(beginWord)
        steps = 0
        if endWord not in s:
            return steps
            

        while q:
            l = len(q)
            steps += 1
            for _ in range(l):
                word = q.popleft()
                if word == endWord:
                    return steps
                
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new = word[:i] + c + word[i+1:]

                        if new not in visited and new in s:
                            q.append(new)
                            visited.add(new)
        return 0