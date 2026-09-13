class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i, (a, b) in enumerate(equations):
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))
        

        def dfs(start, target, product, visited):
            if start == target:
                return product

            visited.add(start)
            for nxt in graph[start]:
                node, value = nxt
                if node not in visited:
                    result = dfs(node, target, product * value, visited)
                    if result != -1:
                            return result
            return -1
        results = []
        for c, d in queries:
            if c not in graph or d not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(c, d, 1.0, set()))

        return results
