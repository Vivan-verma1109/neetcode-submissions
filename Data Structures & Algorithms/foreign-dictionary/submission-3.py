class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        seen = set()

        for i in words:
            for j in i:
                if i not in seen:
                    graph[j] = []
                    seen.add(j)
        print(graph)

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for a, b in zip(w1, w2):
                if a != b:
                    if b not in graph[a]:
                        graph[a].append(b)
                    break

        print(graph)
        res = []
        visiting = set()
        visited = set()

        def dfs(node):
            if node in visited:
                return True
            
            if node in visiting:
                return False

            visiting.add(node)


            for nxt in graph[node]:
                if not dfs(nxt):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            res.append(node)

            return True
        
        for ch in graph:
            if not dfs(ch):
                return ""
        return "".join(res[::-1])