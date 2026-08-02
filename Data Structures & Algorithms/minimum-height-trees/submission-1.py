class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        if n == 1:
            return [0]
        in_degree = [0] * n
        for i in range(n):
            graph[i] = []

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

            in_degree[a] += 1
            in_degree[b] += 1

        queue = deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 1:
                queue.append(i)
        print(queue)
        remaining = n

        while remaining > 2:
            size = len(queue)
            remaining -= size
            for _ in range(size):
                node = queue.popleft()
                for nxt in graph[node]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 1:
                        queue.append(nxt)
        return list(queue)
